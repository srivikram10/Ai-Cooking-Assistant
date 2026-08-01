// ===================================
// AI Cooking Assistant — Frontend JS
// ===================================

// DOM Elements
const foodInput = document.getElementById('food-input');
const langSelect = document.getElementById('lang-select');
const recipeOutput = document.getElementById('recipe-output');
const loadingContainer = document.getElementById('loading-container');
const recipeSection = document.getElementById('recipe-section');
const searchSection = document.getElementById('search-section');
const cookAnim = document.getElementById('cook-anim');

// Cooking emoji cycle for loading animation
const cookingEmojis = ['🍳', '🥘', '🍲', '🫕', '👨‍🍳', '🔥', '🍽️', '✨'];
let emojiIndex = 0;
let emojiInterval = null;

// Enter key triggers search
foodInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') getRecipe();
});

/**
 * Quick search from category chips
 */
function quickSearch(dish) {
    foodInput.value = dish;
    getRecipe();
}

/**
 * Show loading state
 */
function showLoading() {
    loadingContainer.classList.add('active');
    recipeSection.classList.remove('active');
    
    emojiIndex = 0;
    emojiInterval = setInterval(() => {
        emojiIndex = (emojiIndex + 1) % cookingEmojis.length;
        cookAnim.textContent = cookingEmojis[emojiIndex];
    }, 400);
}

/**
 * Hide loading state
 */
function hideLoading() {
    loadingContainer.classList.remove('active');
    if (emojiInterval) {
        clearInterval(emojiInterval);
        emojiInterval = null;
    }
}

/**
 * Show recipe section
 */
function showRecipe() {
    hideLoading();
    recipeSection.classList.add('active');
    recipeSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

/**
 * Go back to search
 */
function goBack() {
    recipeSection.classList.remove('active');
    searchSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    foodInput.focus();
}

/**
 * Convert markdown-like recipe text to beautiful HTML
 */
function renderRecipeHTML(text) {
    if (!text) return '<p>No recipe found.</p>';

    let html = text;

    // Escape HTML first
    html = html.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

    // --- Parse Sections ---

    // H2 headers: ## Title
    html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');

    // H3 headers: ### Section
    html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');

    // Bold: **text**
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');

    // Italic: *text*
    html = html.replace(/(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)/g, '<em>$1</em>');

    // --- Extract and render meta info (Prep Time, Cook Time, Servings) ---
    const metaRegex = /<strong>(Prep Time|Cook Time|Servings):<\/strong>\s*(.+)/g;
    let metaItems = [];
    let match;
    const metaIcons = {
        'Prep Time': '⏱️',
        'Cook Time': '🔥',
        'Servings': '🍽️'
    };

    while ((match = metaRegex.exec(html)) !== null) {
        metaItems.push({
            label: match[1],
            value: match[2].trim(),
            icon: metaIcons[match[1]] || '📌'
        });
    }

    if (metaItems.length > 0) {
        // Remove the meta lines from the main html
        html = html.replace(/<strong>(Prep Time|Cook Time|Servings):<\/strong>\s*.+/g, '');

        // Build meta HTML
        const metaHTML = '<div class="recipe-meta">' +
            metaItems.map(m => 
                `<div class="meta-item">
                    <span>${m.icon}</span>
                    <span class="meta-label">${m.label}:</span>
                    <span class="meta-value">${m.value}</span>
                </div>`
            ).join('') +
            '</div>';

        // Insert after first h2
        html = html.replace('</h2>', '</h2>' + metaHTML);
    }

    // --- Convert ordered lists (numbered steps) ---
    // Find blocks of numbered lines: 1. Step text
    html = html.replace(/((?:^\d+\.\s+.+\n?)+)/gm, (block) => {
        const items = block.trim().split('\n')
            .filter(line => /^\d+\.\s+/.test(line))
            .map(line => `<li>${line.replace(/^\d+\.\s+/, '')}</li>`)
            .join('\n');
        return `<ol>${items}</ol>`;
    });

    // --- Convert unordered lists (ingredients, tips, nutrition) ---
    html = html.replace(/((?:^- .+\n?)+)/gm, (block) => {
        const items = block.trim().split('\n')
            .filter(line => line.startsWith('- '))
            .map(line => `<li>${line.substring(2)}</li>`)
            .join('\n');
        return `<ul>${items}</ul>`;
    });

    // --- Detect and style nutrition section ---
    // Look for the nutrition heading and the ul that follows it
    html = html.replace(
        /(<h3>[^<]*Nutrition[^<]*<\/h3>\s*)<ul>([\s\S]*?)<\/ul>/i,
        (match, heading, listContent) => {
            // Parse nutrition items
            const nutritionItems = listContent.match(/<li>(.+?)<\/li>/g) || [];
            const gridItems = nutritionItems.map(item => {
                const text = item.replace(/<\/?li>/g, '').replace(/<\/?strong>/g, '');
                const parts = text.split(':');
                if (parts.length >= 2) {
                    return `<div class="nutrition-item">
                        <span class="nutrition-value">${parts[1].trim()}</span>
                        <span class="nutrition-label">${parts[0].trim()}</span>
                    </div>`;
                }
                return `<div class="nutrition-item"><span class="nutrition-label">${text}</span></div>`;
            }).join('');

            return heading + '<div class="nutrition-grid">' + gridItems + '</div>';
        }
    );

    // --- Detect and style tips section ---
    html = html.replace(
        /(<h3>[^<]*Tip[^<]*<\/h3>\s*)<ul>([\s\S]*?)<\/ul>/i,
        (match, heading, listContent) => {
            const tipItems = listContent.match(/<li>(.+?)<\/li>/g) || [];
            const tipsHTML = tipItems.map(item => {
                const text = item.replace(/<\/?li>/g, '');
                return `<div class="tip-item">
                    <span class="tip-icon">💡</span>
                    <span>${text}</span>
                </div>`;
            }).join('');
            return heading + tipsHTML;
        }
    );

    // --- Clean up extra newlines ---
    html = html.replace(/\n{3,}/g, '\n\n');

    // Convert remaining single newlines to <br> only if not inside a tag
    html = html.replace(/\n/g, '<br>');

    // Remove excessive <br> around block elements
    html = html.replace(/<br>\s*(<h[23]|<ol|<ul|<div|<\/ol|<\/ul|<\/div)/g, '$1');
    html = html.replace(/(<\/h[23]>|<\/ol>|<\/ul>|<\/div>)\s*<br>/g, '$1');
    html = html.replace(/(<br>\s*){3,}/g, '<br><br>');

    return html;
}

/**
 * Fetch recipe from backend
 */
async function getRecipe() {
    const food = foodInput.value.trim();
    const lang = langSelect.value;

    if (!food) {
        foodInput.focus();
        foodInput.style.borderColor = '#ef4444';
        setTimeout(() => { foodInput.style.borderColor = ''; }, 2000);
        return;
    }

    showLoading();

    try {
        const response = await fetch('/get-recipe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: food, lang: lang })
        });

        const data = await response.json();
        recipeOutput.innerHTML = renderRecipeHTML(data.recipe);
        showRecipe();
    } catch (error) {
        hideLoading();
        recipeOutput.innerHTML = `
            <h2>⚠️ Connection Error</h2>
            <p>Could not reach the server. Please make sure the backend is running and try again.</p>
        `;
        recipeSection.classList.add('active');
        console.error('Recipe fetch error:', error);
    }
}

/**
 * Voice input recipe
 */
async function voiceRecipe() {
    const lang = langSelect.value;

    showLoading();

    try {
        const response = await fetch('/voice-recipe', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ lang: lang })
        });

        const data = await response.json();
        foodInput.value = data.spoken_text;
        recipeOutput.innerHTML = renderRecipeHTML(data.recipe);
        showRecipe();
    } catch (error) {
        hideLoading();
        recipeOutput.innerHTML = `
            <h2>⚠️ Voice Error</h2>
            <p>Could not process voice input. Make sure your microphone is connected and try again.</p>
        `;
        recipeSection.classList.add('active');
        console.error('Voice recipe error:', error);
    }
}