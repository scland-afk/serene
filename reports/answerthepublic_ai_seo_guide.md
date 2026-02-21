# AnswerThePublic for SEO and AI Search Improvement

**Goal:** Show up best in AI answers (Google AI Overviews, Perplexity, ChatGPT, etc.) by making copy **quotable**, **location-specific**, and **query-matching**.

---

## Why the rewrite works

| Before | After | Why it helps AI |
|--------|--------|------------------|
| "Most paving stone patios range from $35 to $45 per square foot" | "Paving stones in Edmonton cost $35 to $45 per square foot" | AI systems look for **direct, complete answers** to queries like "how much do paving stones cost in Edmonton." The second sentence is a **one-sentence quote**: it includes location (Edmonton), topic (paving stones), and number ($35–$45). Generic "most … range from" is harder to cite. |

### Principles

1. **Mirror the query.** People (and AI) ask "How much do paving stones cost in Edmonton?" → Your sentence should contain "[thing] in [place] cost [number]."
2. **One clear fact per sentence.** Makes it easy for AI to extract and attribute.
3. **Name the location.** Edmonton (or St. Albert, Sherwood Park) in the claim so you rank for local AI answers.
4. **Use question phrases from AnswerThePublic.** If the tool shows "paving stones cost," "paving stones Edmonton," "how much paving stones," bake those into the sentence naturally.

---

## How to use AnswerThePublic for AI-friendly copy

1. **Run seeds** for each service + location, e.g.:
   - "paving stones Edmonton"
   - "sod installation cost Edmonton"
   - "retaining wall cost Edmonton"
   - "snow removal Edmonton"
2. **Export questions and prepositions.** Look for:
   - **Questions:** "How much do … cost?", "What does … cost in Edmonton?", "Is … expensive?"
   - **Prepositions:** "[service] cost," "[service] Edmonton," "[service] price"
3. **Turn one high-intent phrase into a single-sentence answer** and put it in body copy and/or FAQ/JSON-LD.
   - Example: "paving stones cost Edmonton" → **"Paving stones in Edmonton cost $35 to $45 per square foot."**
4. **Repeat for other services.** Pattern: **[Service] in [Edmonton / area] cost [range].** Optional second sentence for caveats (access, quote after visit).

---

## Copy pattern for cost and fact statements

- **Generic (weak for AI):** "Most [X] range from $Y to $Z …"
- **AI-friendly:** "[X] in Edmonton cost $Y to $Z [per unit]. [Optional: one short caveat or CTA.]"

Apply the same idea to:

- **Sod:** "Sod installation in Edmonton costs $0.70 to $2.50 per square foot …"
- **Retaining walls:** "Retaining walls in Edmonton cost $45 to $85 per square foot of wall face …"
- **Artificial grass, landscape design:** Lead with "[Service] in [location] cost [range]" or "run from [range]" when you have a number.

---

## Checklist for AI visibility

- [ ] Cost/fact sentences include **location** (Edmonton, St. Albert, Sherwood Park) where relevant.
- [ ] Wording matches how people ask (use AnswerThePublic questions as a source).
- [ ] One clear, quotable sentence per key fact; avoid burying the number in long paragraphs.
- [ ] FAQ and JSON-LD `acceptedAnswer` text use the same AI-friendly phrasing.
- [ ] Refresh AnswerThePublic (or similar) every few months and add new question-based sentences.

---

## Applied in this project

- **Paving stones** (`/services/paving-stones/`): "Paving stones in Edmonton cost $35 to $45 per square foot." FAQ question: "How much do paving stones cost in Edmonton?"
- **Snow removal** (`/services/snow-removal/`): "Residential snow removal in Edmonton costs from $70 per visit or from $200 per month for seasonal contracts." Added FAQs from AI prompts: free quote, what's included (sidewalks/driveways), emergency snow removal, book snow shoveling service. Pricing section: "Snow plowing service Edmonton prices." Schema updated with Edmonton-specific Q&A.
- **Commercial snow removal** (`/commercial-snow-removal/`): Lead pricing sentence and phrases: "Commercial snow removal contractors Edmonton," "Snow plowing service Edmonton prices," "Emergency snow removal Edmonton." Schema description updated.
- **Sod installation** (`/services/sod-installation/`): "Sod installation in Edmonton costs $0.70 to $2.50 per square foot installed."
- **Final grading** (`/services/final-grading/`): "Final grading in Edmonton costs $1,500 to $3,500 for most residential lots."
- **Residential landscaping** (`/residential-landscaping/`): Cost list uses Edmonton-qualified sentences; FAQ answer includes sod, paving, final grading costs in Edmonton.
- **Blog** (`prepare-snow-removal-edmonton`): Added quotable cost sentence for snow removal in Edmonton near the top.

Use the same pattern when you add or edit other services (retaining walls, artificial grass, etc.).
