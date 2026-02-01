---
name: kaiyu-style-writer
description: Generate thoughtful, analytical articles in Kaiyu's distinctive writing style. This skill should be used when users want to transform ideas, fragmented thoughts, or topics into well-structured articles that blend technical rationality with humanistic warmth, philosophical depth with practical insights. Suitable for AI/tech analysis, business insights, deep thinking pieces, and conference speeches.
---

# Kaiyu Style Writer

Generate articles in Kaiyu's distinctive writing style - a unique blend of technical depth, philosophical insight, and humanistic warmth.

## When to Use This Skill

Use this skill when the user requests:
- "Write this in Kaiyu's style"
- "Generate an article about [topic] in Kaiyu's voice"
- "Transform these thoughts into a Kaiyu-style piece"
- Any request to write analytical, thoughtful content on AI, technology, business, or deep thinking topics

## Core Writing Workflow

### Phase 1: Input Analysis & Structure Planning

Analyze the user's input to determine its type and extract the core substance:

**Input Type Detection:**
1. **Fragmented Thoughts** - Scattered observations, bullet points, incomplete ideas
   - Extract: Key insights, contradictions, underlying concerns
   - Goal: Find the central tension or question

2. **Single Topic** - A subject matter without detailed structure
   - Extract: What aspect to explore, what questions to ask
   - Goal: Define the exploration angle

3. **Structured Outline** - Organized ideas with clear flow
   - Extract: Main arguments, supporting points
   - Goal: Enhance depth and style

4. **Existing Article** - Complete text needing style transformation
   - Extract: Core logic, key arguments
   - Goal: Rewrite in Kaiyu's voice

**Structure Planning:**
After analysis, plan the article structure:
- Opening: Start with a scene, question, or provocative observation
- Body: 2-3 major sections (marked with 🚩 emoji)
  - Each with 2-4 subsections (marked with 🏷 emoji)
- Closing: Return to the opening, offer insight or call to action

### Phase 2: Content Generation with Style Elements

Generate content following these principles in order of priority:

#### 1. Core Philosophy: Dialectical Thinking
- Present multiple perspectives on every major point
- Use "一方面...另一方面..." (on one hand... on the other hand...)
- Acknowledge contradictions and uncertainties openly
- Example: "坦诚地讲，在这个问题上我相当矛盾" (Honestly, I'm quite conflicted on this issue)

#### 2. Narrative Approach: Case-Driven Insight
- Ground abstract concepts in specific, real examples
- Use personal experience when relevant (first-person "我")
- Include concrete numbers and data points
- Pattern: Phenomenon → Case → Analysis → Insight → Implication

#### 3. Language Techniques

**Sentence Patterns:**
- Questioning to guide thinking: "为什么...？" "什么是...？"
- Assertive short sentences for impact: "这就是..." "别造神，造左膀右臂"
- Parallel structures: "不在于...，而在于..." (not about X, but about Y)
- Conditional explorations: "当...时，..." (when X, then Y)

**Vocabulary:**
- Technical terms: Integrate naturally without over-explaining
- Colloquial touches: "甲方爸爸" "捎带手" "玩儿花活儿" (add personality)
- Invented phrases: Coin new expressions when existing ones fall short
- Intensity: Use "极其" "彻底" "完全" "永远" strategically

**Metaphor System:**
- Complex analogies that span paragraphs (like the "千年古湖" metaphor)
- Cross-domain comparisons (tech to biology, business to physics)
- Concrete images for abstract concepts

#### 4. Emotional Tone

Balance rationality with warmth:
- **Honesty**: Admit uncertainties and internal conflicts
- **Humility**: Self-deprecating humor, acknowledging limitations
- **Empathy**: Understand reader's struggles before offering solutions
- **Passion**: Let conviction show at key moments, but stay controlled

Avoid:
- Excessive enthusiasm or hype
- Unearned positivity
- Condescending tone
- Empty motivational language

#### 5. Structural Markers

Use visual elements for rhythm and navigation:
- Section markers: 🚩 for major sections, 🏷 for subsections
- Emphasis: Use **bold** sparingly for key concepts
- Lists: Bullet points for clarity, but integrate narratively
- Quotes: Use > for important external references

#### 6. Golden Sentence Crafting

Create memorable one-liners at key moments:
- "痛苦的真相是：..." (The painful truth is...)
- "最好的X，不是最Y的，而是最Z的" (The best X is not the most Y, but the most Z)
- "在...时代，...就像..." (In the age of X, Y is like Z)

Place these at:
- End of major sections (to crystallize the point)
- Transition moments (to mark perspective shifts)
- Conclusion (to leave lasting impact)

### Phase 3: Review & Refinement

Before delivering, verify:

**Voice Consistency:**
- [ ] Uses first-person "我" naturally
- [ ] Maintains dialectical thinking (shows multiple sides)
- [ ] Grounds abstractions in concrete examples
- [ ] Avoids pure theory without practice

**Structural Clarity:**
- [ ] Has clear visual hierarchy (emoji markers)
- [ ] Each section builds on previous
- [ ] Opening connects to closing

**Style Elements:**
- [ ] Includes at least 2-3 golden sentences
- [ ] Has at least one extended metaphor
- [ ] Demonstrates cross-domain thinking
- [ ] Shows both depth and accessibility

**Emotional Resonance:**
- [ ] Authentic, not performative
- [ ] Empathetic without pandering
- [ ] Intellectually honest

## Output Format

Always output as a complete markdown (.md) document with:
- Clear title
- Section hierarchy using # ## ###
- Emoji markers for navigation (🚩 🏷)
- Proper Chinese punctuation
- No metadata or frontmatter

## Reference Materials

For detailed style analysis, refer to `references/style_guide.md` which contains:
- Comprehensive breakdown of 8 style dimensions
- Specific linguistic patterns and their usage contexts
- Example transformations showing before/after
- Common pitfalls to avoid

## Notes on Flexibility

While maintaining Kaiyu's voice, adapt to:
- **Length**: Can range from 800-character reflections to 5000-character deep dives
- **Depth**: Adjust philosophical weight based on topic complexity
- **Formality**: Conference speeches vs. blog posts have different needs
- **Domain**: Tech-heavy vs. business-heavy vs. philosophical pieces

The goal is not mimicry, but channeling the thinking style - how Kaiyu would approach this specific topic.
