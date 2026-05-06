# Presentation content and design plan for A Survey of Adversarial Learning on Graphs

## Presentation strategy

The strongest story arc for this talk is: **graphs are useful, graph models are vulnerable, the literature became messy, and this survey’s real contribution is to impose structure on that mess**. Start with the intuitive vulnerability from the paper’s own opening example, then move quickly into the minimum notation needed to read the rest of the survey, and after that organise the body around a repeated question: **what is being optimised, what is being perturbed, what is being assumed, and how is success measured?** That lets the audience see attacks and defenses as two sides of the same optimisation-and-constraints picture rather than as a long list of unrelated papers. This is faithful to the survey’s stated goals: unify formulations, define taxonomies, summarise metrics, and end with open problems. citeturn4view0turn5view0turn7view0turn7view2turn7view6turn7view9turn7view10turn7view11

The conceptual thread that should keep the room oriented is **“small graph perturbations under constraints”**. Everything should keep returning to that phrase. In the preliminaries, it explains why the paper spends time on graph notation and on node-, link-, and graph-level tasks. In the attack section, it becomes the outer maximisation problem with a perturbation space and similarity/budget constraints. In the defense section, it flips direction into a minimisation problem that aims to stay stable on clean or perturbed graphs. In the metrics section, it turns into three practical questions: did the perturbation work, what did it cost, and how visible was it? That thread is already latent in the survey; the slides should make it explicit. citeturn5view0turn7view1turn7view2turn10view1turn10view2turn7view6turn8view5turn9view0

For balance, spend **just enough time on basics to unlock the rest**. The audience is mathematically strong, so do not over-explain what a graph is, but do explain the paper’s specific assumptions: simple graphs by default, the task split, and inductive versus transductive settings. Then give formulas only where they clarify the framing: the generic task loss, the unified attack objective, the poisoning/evasion distinction, the strategy-specific constraints, the unified defense objective, and two or three metrics that matter. Taxonomies should be shown as clean visual maps, not as paragraphs. The large survey tables should only appear as compressed, representative matrices. The toy graph example should return repeatedly so the talk never feels like a taxonomy dump. citeturn5view0turn7view1turn7view2turn10view1turn10view2turn7view6turn8view5

To prove that you genuinely read the paper without overloading the audience, mirror the paper’s section order very closely, reuse its two core visual intuitions in redesigned form, keep the paper’s distinctions exactly where the authors place them, and surface the details that only someone who read the survey would notice: the “simple graph” default, the fact that targeted attack in this survey is defined by **attack range** rather than **specific label**, the overlap tension between adversarial- and objective-based defenses, and the paper’s unusual emphasis on metrics and evaluation as first-class survey content rather than an afterthought. Those details will read as “I understood the paper”, not just “I skimmed the abstract”. citeturn5view0turn10view0turn10view4turn7view9turn9view1

For pacing, aim for roughly **44 minutes of speaking plus about 1 minute of natural slack**. A good split is: 6–7 minutes for introduction and preliminaries, 15–16 minutes for attacks, 11–12 minutes for defenses, 4–5 minutes for metrics, 4 minutes for open problems, and 2 minutes for conclusion. That leaves just enough room for small pauses, one or two transitions, and potential projector friction without creating a dead Q&A block.

## Design system

Because the paper is a **16-page survey with only two main figures and three large tables**, your deck should not visually depend on screenshots from the PDF. It should instead **redraw the paper’s core ideas in a cleaner presentation language** while keeping the content aligned with the source. citeturn4view0turn11view0turn11view1

### Background style

Use a **white background** throughout. Reserve tinted panels for formulas, taxonomy cards, and compact method matrices. Avoid full-bleed colour slides. The deck should feel like a modern technical seminar, not a poster.

### Colour roles

Use colour by **semantic role**, not decoration.

- **Neutral framework**: charcoal, slate, and light grey for text, graph outlines, and inactive elements.
- **Attack colour**: coral to red. Use this for perturbations, maximisation arrows, attacker-controlled variables, suspicious edges, and attack section tags.
- **Defense colour**: teal to blue-green. Use this for protective operations, minimisation arrows, robust training, structure redesign, and defense section tags.
- **Metrics colour**: muted purple for evaluation content.
- **Preliminary colour**: warm amber or ochre for setup slides.
- **Warning/caveat colour**: soft yellow for limitations and note boxes.

The key is consistency: once red means “attack-side intervention”, it should never later mean “good result”.

### Typography hierarchy

- **Slide titles**: large, left-aligned, short, 1 line when possible.
- **Section tag**: small coloured pill above the title, e.g. “Attack formulation”.
- **Body text**: no smaller than projector-safe medium size; prefer 3–5 bullets maximum.
- **Formula labels**: large enough to read from the back, with a caption immediately under or beside them.
- **Captions and notes on-slide**: minimal and compact.

Use a modern sans-serif look for titles and body. Formula text can remain standard mathematical typesetting visually, but the surrounding labels should stay sans-serif to keep the deck contemporary.

### Diagram conventions

Use one visual grammar for all custom diagrams:

- Nodes as circles with consistent stroke thickness.
- Benign nodes in light neutral fills.
- Target node with a dark ring.
- Changed edges in attack colour.
- Pruned or protected edges in defense colour.
- Feature perturbations as tiny square or bar badges beside nodes.
- Model blocks as rounded rectangles or circles, never clip-art style.
- Constraint symbols such as `Δ`, `Q(·,·)`, and shields shown as small callout badges rather than as floating text.

### Attack versus defense distinction

Make the contrast visceral:

- **Attack slides**: warm accent bar, red/orange highlights, “maximise” iconography, plus signs and rewiring arrows.
- **Defense slides**: cool accent bar, teal/green highlights, shields, pruning scissors, smoothing or aggregation visuals, “minimise/stabilise” iconography.

This attack/defense colour role should be visible even if someone tunes out the labels.

### Showing graph perturbations

Graph perturbations should be shown with three distinct micro-encodings:

- **Added edge**: thick red line with a small `+`.
- **Removed edge**: faint grey edge with red strike-through or faded dotted trail.
- **Feature flip/change**: one or two small coloured squares or bars near the node, with changed entries highlighted.

That lets you explain structure attack, feature attack, and hybrid attack without changing the entire visual language.

### Showing taxonomies

Do not use dense trees with tiny text. Use **taxonomy strips** or **card grids**.

- For **attack taxonomy**, use a horizontal strip with seven buckets: knowledge, goal, capability, strategy, manipulation, algorithm, target task.
- For **defense taxonomy**, use a two-row card grid: preprocessing, structure, adversarial, objective, detection, hybrid, plus a smaller “other tasks” side card.

Each bucket should contain at most three keywords or chips. Details come on later slides.

### Showing formulas

Every formula should sit inside a **soft grey formula card** with one accent colour applied only to the symbols under discussion.

Recommended annotation style:

- **Given / fixed** objects in neutral grey.
- **Attacker-controlled** terms in attack colour.
- **Defender-controlled** terms in defense colour.
- A short English gloss directly beneath:
  - what is optimised,
  - what is controlled,
  - what the constraint means.

Do not place full equations on raw white space with no annotation. The audience can handle math; they should not have to decode presentation intent at the same time.

### Showing survey tables without unreadability

Never paste the full original tables. Compress them into one of two formats:

- **Representative matrix** for method summaries.
- **Grouped method cards** if the comparison is more conceptual than tabular.

Use at most 5–6 columns. Replace verbose dataset and baseline lists with tiny task/dataset chips or move those details into speaker notes.

### Callouts, section cards, and summary slides

Use callouts for three things only:

- “What changes?”
- “What stays fixed?”
- “Why this matters?”

Use section cards sparingly. Because the target length is only 45 minutes, a full standalone divider slide is only worth it if it gives the audience a mental reset. A better compromise is to embed a **section pill plus thin progress ribbon** into the first slide of each new block.

Summary slides should not repeat everything. They should answer one synthesis question, such as:
- “What have attacks mostly assumed so far?”
- “How do defense categories differ in where they intervene?”
- “Which metrics are actually worth remembering?”

### Keeping consistency across the deck

Keep the following fixed across all 24 slides:

- title placement,
- section pill placement,
- progress ribbon,
- node and edge drawing style,
- formula-card style,
- card corner radius,
- icon style,
- attack/defense colour semantics,
- recurring toy graph.

That consistency is what will make an intellectually dense talk feel controlled rather than crowded.

## Slide-by-slide plan

### Opening block

This opening block should mirror the paper’s introduction and preliminary sections: motivation, the survey’s need for unified definitions and metrics, the notation actually required for the rest of the talk, and the split into node-, link-, and graph-level tasks with inductive/transductive learning as the crucial training distinction. citeturn4view0turn5view0turn7view0turn7view1

**Slide 1 — Title slide**

- **Time:** 1.0 min
- **Purpose:** Set expectations and frame the talk as a guided reading of a survey, not a pitch for one model.
- **Visible content:**
  - *A Survey of Adversarial Learning on Graphs*
  - *Attacks, defenses, metrics, and open problems*
  - Your name, course, date
- **Layout / UI plan:** Title top-left. Subtitle directly underneath in smaller type. Bottom-left metadata line for your name/course. Right half: minimalist graph icon with one highlighted target node and two accent edges.
- **Visual:** Clean custom graph motif; one node ringed dark to foreshadow the target node theme.
- **Speaker notes:** “Today I’m presenting a survey paper rather than a single method paper. So my job is slightly different: I want to show the logic of the field, not just one architecture. The paper’s contribution is mainly organisational. It tries to unify how we talk about adversarial attacks and defenses on graphs, how we categorise them, and how we evaluate them. I’ll follow the paper’s order quite closely so it feels like a guided tour rather than a remix.”
- **Avoid:** A long abstract paragraph or a crowded title slide with affiliations and multiple logos.

**Slide 2 — Why adversarial learning on graphs matters**

- **Time:** 2.0 min
- **Purpose:** Make the vulnerability intuitive before formalism starts.
- **Visible content:**
  - *Deep graph learning is powerful — and vulnerable*
  - *Small changes to edges or features can flip a prediction*
  - Chips: *node classification* · *link prediction* · *graph classification*
- **Layout / UI plan:** Left 60%: redesigned version of the paper’s Figure 1 idea, showing clean graph → perturbation → misclassification. Right 40%: three application chips and one big takeaway callout.
- **Visual:** Recurring toy graph in three stages. Perturbations in coral. Prediction chip changes colour after perturbation.
- **Speaker notes:** “The easiest way into this topic is the paper’s own first figure. The point is not that graphs are fragile in a vague sense. The point is that very small, structured changes — maybe only a few edges, maybe a few feature entries — can change the model’s output. And unlike images, the attack surface is not just pixels. On graphs, you can change structure, features, or both. The survey starts from that intuition, and I think the talk should too.”
- **Avoid:** A generic speech about adversarial machine learning in vision that delays the graph-specific point.

**Slide 3 — What this survey is trying to do**

- **Time:** 1.5 min
- **Purpose:** Explain the paper’s value proposition and give the audience a roadmap.
- **Visible content:**
  - Four cards:
    - *Unified formulations*
    - *Attack taxonomies*
    - *Defense taxonomies*
    - *Metrics and open problems*
  - Bottom strip: *Intro → Preliminary → Attacks → Defenses → Metrics → Discussion → Conclusion*
- **Layout / UI plan:** 2×2 card grid in the centre. Thin paper-order ribbon across the bottom, with today’s path highlighted.
- **Visual:** Each card gets a simple icon: equation, branching tree, shield, ruler.
- **Speaker notes:** “This survey argues that the field had two main problems. First, people were using incompatible formulations and assumptions. Second, evaluation was fragmented. So the survey’s main move is to standardise the language: define attacks in a unified way, define defenses in a unified way, classify both, then discuss metrics and research gaps. That is the backbone I’ll keep following.”
- **Avoid:** Listing all contributions as prose copied from the paper.

**Slide 4 — Graph setup used in the paper**

- **Time:** 2.0 min
- **Purpose:** Give only the notation and assumptions needed later.
- **Visible content:**
  - `G = (V, E)`
  - `A`: adjacency matrix
  - `X`: node feature matrix
  - *Default scope in this paper:* *undirected* · *unweighted* · *static* · *homogeneous*
  - *Target instance `t` can be a node, edge, or graph*
- **Layout / UI plan:** Left column for notation. Right column for four assumption chips. Bottom bar for “why this matters later”.
- **Visual:** Small graph with an adjacency matrix inset and a feature matrix inset, both minimal.
- **Speaker notes:** “I only want to introduce the symbols that later formulas actually use. The important thing is not the whole notation table. The important thing is the modelling scope. In this survey, unless stated otherwise, ‘graph’ usually means a fairly simple graph: undirected, unweighted, static, and homogeneous. That matters because some open problems later are exactly about moving beyond those assumptions.”
- **Avoid:** Reproducing the full notation table from the paper.

**Slide 5 — Tasks and learning settings**

- **Time:** 2.0 min
- **Purpose:** Show what the downstream tasks are and why the paper keeps referring to node-, link-, and graph-level settings.
- **Visible content:**
  - *Node-level:* node classification
  - *Link-level:* link prediction
  - *Graph-level:* graph classification / clustering
  - *Training settings:* *inductive* vs *transductive*
  - Bottom formula strip: `L = (1/|V_L|) Σ_{v_i∈V_L} L(f_θ(G,X), y_i)`
- **Layout / UI plan:** Three horizontal task cards across the top. Bottom formula card with two short annotations.
- **Visual:** Left task card shows highlighted node, middle shows candidate edge, right shows whole-graph thumbnail.
- **Speaker notes:** “The paper organises graph analysis into node-, link-, and graph-level tasks. That ends up mattering a lot, because attack methods and defense methods are not evenly distributed across those tasks. Also, the inductive versus transductive distinction matters especially for poisoning. In transductive settings, test nodes are present during training, which makes training-time perturbations particularly relevant. The formula here is just the generic supervised objective. It is the baseline that the later attack and defense objectives will wrap around.”
- **Avoid:** Multiple task-specific formulas. One generic objective is enough.

**Slide 6 — The toy example to keep in mind**

- **Time:** 2.0 min
- **Purpose:** Establish the recurring visual intuition that will anchor later taxonomy slides.
- **Visible content:**
  - *Clean prediction*
  - *Small perturbation*
  - *Wrong prediction*
  - Labels: *topology change* · *feature change* · *budget* · *imperceptibility*
- **Layout / UI plan:** Large centre graphic spanning most of the slide. Very little text. Tiny legend at the bottom assigning attack and defense colours.
- **Visual:** Six-node graph. Dark-ringed target node. Two or three influencer nodes. One attacked version with added red edges and one or two changed feature badges.
- **Speaker notes:** “I’ll keep coming back to this same toy graph so the talk does not become abstract. Think of this target node as the thing the attacker cares about. In the clean graph, the prediction is correct. After a very small perturbation — maybe an edge addition, maybe a feature flip, maybe both — the prediction changes. That is enough to define the whole rest of the talk: who is choosing those perturbations, under what constraints, with what information, and how we try to defend against them.”
- **Avoid:** A toy graph that is unrelated to later slides.

### Attack block

This block corresponds to the paper’s attack section: unified attack formulation, imperceptibility constraint, multi-axis attack taxonomy, the poisoned-versus-evasion split, strategy/manipulation/algorithm choices, representative methods from the large attack table, and the paper’s own summary of current limitations. citeturn7view2turn7view3turn10view0turn10view1turn10view2turn10view3turn6view4turn8view0turn11view0

**Slide 7 — A unified formulation of attack**

- **Time:** 2.5 min
- **Purpose:** Present the paper’s central attack formulation and make it readable.
- **Visible content:**
  - Full or slightly simplified version of Eq. (2)
  - Bottom callout: `Q(Ĝ^{t_i}, G^{t_i}) < ε`
  - Four labels:
    - *attacker chooses perturbed graph*
    - *goal: maximise loss on targets `T`*
    - *inner problem: model parameters come from training*
    - *constraint: stay close to the clean graph*
- **Layout / UI plan:** Formula card on the left occupying about 60% width. Right-side stacked annotation cards. Bottom strip for imperceptibility constraint.
- **Visual:** Use attack colour only on `Ĝ`, `Ψ(G)`, and the outer “maximise”; keep the rest neutral.
- **Speaker notes:** “This is the paper’s first really important equation. Conceptually it is a bilevel problem. The outer level is the attacker: choose a perturbed graph inside some allowed perturbation space. The objective is to increase loss on the target instances. The inner level says the model parameters come from training. So the attack is not floating in a vacuum; it is defined relative to a trained or trainable model. Then the paper adds a second idea: the attack should remain hard to notice, which is why the similarity function `Q` and threshold `ε` matter.”
- **Avoid:** Showing the equation with all symbols in one colour and no explanation.

**Slide 8 — Attack taxonomy in one view**

- **Time:** 1.5 min
- **Purpose:** Give the audience the full map before visiting categories one by one.
- **Visible content:**
  - *Knowledge*
  - *Goal*
  - *Capability*
  - *Strategy*
  - *Manipulation*
  - *Algorithm*
  - *Target task*
- **Layout / UI plan:** One horizontal taxonomy strip with seven rounded cards. Each card contains 2–3 keywords only.
- **Visual:** Each card has a small icon: eye/lock, bullseye, clock, graph edges, wrench, gradient symbol, task dot.
- **Speaker notes:** “This is the attack-side mental map. I would not overload this slide. Its job is just to tell the room that the paper is not using one taxonomy; it is using several axes at once. That is why graph adversarial learning can feel confusing on first read. A method can be white-box, targeted, poisoning, topology-based, rewiring-based, gradient-driven, and aimed at node classification — all at the same time.”
- **Avoid:** Method names. This slide is taxonomy only.

**Slide 9 — What attackers know and what they want**

- **Time:** 2.5 min
- **Purpose:** Cover knowledge assumptions and goal distinctions, including one subtle terminology point likely to impress the lecturer.
- **Visible content:**
  - *Model knowledge:* white-box · grey-box · black-box
  - *Data knowledge:* perfect · moderate · minimal
  - *Goals:* availability vs integrity
  - *Specificity:* targeted vs non-targeted
  - *Error:* specific vs unspecific
  - Small note: *In this survey, “targeted” means target range, not target label*
- **Layout / UI plan:** Left half: vertical knowledge ladder. Right half: 2×2 goal matrix. Bottom thin note strip for the terminology caveat.
- **Visual:** Progressively closed lock icons on the left; crosshair and label tags on the right.
- **Speaker notes:** “I’d linger briefly on the terminology note at the bottom, because it is easy to miss and it matters. In some adversarial ML literature, targeted means ‘push the system to a specific wrong label’. In this survey, targeted attack is defined by attack range — usually a specific subset or a single target node. Error specificity is treated separately. That distinction is subtle, but it shows you actually read the survey closely.”
- **Avoid:** Turning black-box into a long discussion of query complexity.

**Slide 10 — Poisoning versus evasion**

- **Time:** 2.0 min
- **Purpose:** Show the stage-of-intervention distinction both visually and mathematically.
- **Visible content:**
  - *Poisoning = training-time attack*
  - *Evasion = test-time attack*
  - Tiny formula contrast:
    - *Poisoning:* retrain on perturbed graph
    - *Evasion:* parameters fixed after clean training
- **Layout / UI plan:** Left two-thirds: redesigned version of the paper’s Figure 2 pipeline. Right one-third: small equation contrast card with the changed training line highlighted.
- **Visual:** Two arrows: one from perturbed graph back into training, one directly into a copied fixed model.
- **Speaker notes:** “This distinction is conceptually simple but very important. In poisoning, the graph is modified before or during training, so the model is retrained on poisoned data. In evasion, the model is already trained and the attacker only manipulates the test-time input. On graphs, poisoning gets a lot of attention because transductive settings make it natural for test nodes to appear during training. Presentation-wise, this slide should be very visual. The figure does half the work.”
- **Avoid:** Two full equations stacked without pointing out the one line that changes.

**Slide 11 — What can be perturbed and how**

- **Time:** 2.5 min
- **Purpose:** Explain strategy, manipulation, and algorithmic family in one compact slide.
- **Visible content:**
  - *Strategy:* topology · feature · hybrid
  - *Manipulation:* add · remove · rewire
  - *Algorithms:* gradient-based · genetic · reinforcement learning · generative
  - *Budget:* `Δ`
- **Layout / UI plan:** Three columns:
  - left for strategy,
  - middle for manipulation,
  - right for algorithm family.
  Bottom budget callout spanning the slide.
- **Visual:** Use the recurring toy graph with three micro-overlays: an added edge, a removed edge, and a rewiring pair. Beside it, tiny feature badges toggled on/off.
- **Speaker notes:** “I’d present this as three orthogonal questions. First, what part of the graph is attacked: structure, features, or both? Second, what operation is allowed: add, remove, or rewire? Rewiring is especially nice to show because it preserves some graph statistics better and can look less obvious. Third, how is the attack actually found? Often by gradients, but because graphs are discrete, gradients usually guide a choice rather than directly modify the input the way they do in images.”
- **Avoid:** A catalogue of all optimisation tricks from individual papers.

**Slide 12 — Representative attack methods**

- **Time:** 3.0 min
- **Purpose:** Compress the attack table into something readable and memorable.
- **Visible content:**
  - Compact matrix with rows:
    - *Nettack*
    - *Meta-Self / Meta-Train*
    - *PGD / Min-Max*
    - *RL-S2V*
    - *IGA*
    - *ReWatt*
  - Columns:
    - *Family*
    - *Task*
    - *Perturbation*
    - *Why it matters*
  - Footer: *Representative only — the paper’s full table is much broader*
- **Layout / UI plan:** One central compact matrix. Task dots or chips in the first or second column. One highlighted row per task family.
- **Visual:** Task chips in three colours: node, link, graph.
- **Speaker notes:** “I would not try to read the original survey table aloud. Instead I’d use representative anchor methods. Nettack is historically important for node attacks. Meta-Self and PGD show optimisation-based poisoning or topology perspectives. RL-S2V shows the reinforcement learning angle. IGA gives us a link-prediction representative, and ReWatt gives us a graph-level representative. That is enough to signal breadth without turning the talk into a bibliography recital.”
- **Avoid:** Full baseline lists, full dataset lists, or every row from Table II.

**Slide 13 — What the attack literature still misses**

- **Time:** 2.0 min
- **Purpose:** Conclude the attack section with the paper’s own limitations.
- **Visible content:**
  - *Unnoticeability*
  - *Scalability*
  - *Realistic knowledge assumptions*
  - *Real-world / physical realism*
  - Bottom transition line: *Now switch perspective: how does the paper frame defense?*
- **Layout / UI plan:** 2×2 grid of limitation cards. Tiny transition ribbon at the bottom.
- **Visual:** Each card gets an icon: eye, scale/network, lock, real-world environment.
- **Speaker notes:** “The survey is fairly clear that attack performance alone is not enough. Many methods work on small citation graphs, assume strong knowledge, and treat low budget as if that automatically means low detectability. The paper explicitly pushes back on that. So I’d end the attack block by saying: the field got good at making attacks work in benchmark settings, but the harder questions are stealth, scale, weaker prior knowledge, and realism.”
- **Avoid:** Adding external criticisms that are not already in the paper’s framing.

### Defense block

This block follows the paper’s defense section: a unified defense optimisation problem, the six-way defense taxonomy, representative defense families, the dominance of node-classification settings, and the paper’s summary of current limitations and research opportunities. citeturn7view6turn7view7turn10view4turn10view5turn6view5turn7view8turn8view2turn11view1

**Slide 14 — A unified formulation of defense**

- **Time:** 2.0 min
- **Purpose:** Present the defense-side analogue to the attack formulation.
- **Visible content:**
  - Simplified Eq. (9)
  - Three labels:
    - *defender minimises loss*
    - *must work on clean or perturbed graphs*
    - *same graph setting, opposite optimisation direction*
- **Layout / UI plan:** Left: formula card. Right: comparison panel with “Attack = maximise” versus “Defense = minimise”.
- **Visual:** Use two vertical arrows, coral pointing up for maximise and teal pointing down for minimise.
- **Speaker notes:** “I’d present this as the mirror image of the previous formulation. The attacker wants to increase loss on chosen targets under perturbation constraints. The defender wants performance to remain stable whether the graph is clean or has been perturbed. Framed this way, attack and defense become symmetric in the talk, which helps the audience keep track of the paper’s structure.”
- **Avoid:** Lots of new notation beyond what was already introduced on the attack slide.

**Slide 15 — Defense taxonomy in one view**

- **Time:** 1.5 min
- **Purpose:** Give the audience the defense map before details.
- **Visible content:**
  - *Preprocessing-based*
  - *Structure-based*
  - *Adversarial-based*
  - *Objective-based*
  - *Detection-based*
  - *Hybrid*
  - Side note: *plus a small “others” bucket*
- **Layout / UI plan:** Two-row card grid with six main cards and one smaller side card.
- **Visual:** Shield-themed cards in the defense palette.
- **Speaker notes:** “Attacks were organised across several axes. Defenses are simpler in this survey: they are mostly categorised by where or how they intervene. Do they clean data first? Change the model architecture? Train adversarially? Change the objective? Detect malicious perturbations? Or combine several of these?”
- **Avoid:** Examples inside every card. That comes next.

**Slide 16 — Clean the graph or change the model**

- **Time:** 2.0 min
- **Purpose:** Cover preprocessing- and structure-based defenses together.
- **Visible content:**
  - *Preprocessing:* remove suspicious edges before training
  - *Structure-based:* redesign message aggregation or convolution
  - *Representative methods:* Drop edges · RGCN · AGCN · PA-GNN
- **Layout / UI plan:** Left half for preprocessing with a graph-cleaning visual. Right half for structure-based with a stylised aggregation block diagram.
- **Visual:** Left: malicious red edge gets pruned into teal/grey output graph. Right: robust aggregation box with weighted incoming edges.
- **Speaker notes:** “These two families defend at different stages. Preprocessing tries to stop bad structure from ever reaching the model. Structure-based defense accepts the graph but changes the architecture so message passing is less brittle. I’d mention examples, but the key story is the intervention point: before learning versus inside the model.”
- **Avoid:** Definitions copied verbatim from the paper.

**Slide 17 — Train against attacks or change the objective**

- **Time:** 2.0 min
- **Purpose:** Cover adversarial-based and objective-based defenses, including their overlap.
- **Visible content:**
  - *Adversarial-based:* train with adversarial goals or adversarial examples
  - *Objective-based:* redesign the loss / regularisation for robustness
  - *Representative methods:* VAT/BVAT · GraphDefense · r-GCN/VPN · SCEL/SD
  - Small note: *These categories partially overlap*
- **Layout / UI plan:** Left: training loop diagram with adversarial example generation. Right: objective card with regularisation terms highlighted.
- **Visual:** Teal training loop, with one small coral arrow showing adversarial data entering the loop.
- **Speaker notes:** “This is where I’d include one subtle critique in my notes, not on the slide: the paper itself admits the boundary between adversarial-based and objective-based defenses is not perfectly clean. That is actually useful to mention verbally, because it shows you are not treating the taxonomy as absolute. Still, as a teaching device, the split works: some defenses get robustness by training against attacks, others by changing what the model is encouraged to optimise.”
- **Avoid:** A full min-max derivation. The conceptual distinction is enough here.

**Slide 18 — Detect, certify, and combine**

- **Time:** 3.0 min
- **Purpose:** Finish the defense taxonomy, compress the defense table, and connect to limitations.
- **Visible content:**
  - *Detection / certification:* monitor, detect, or certify robustness
  - *Hybrid:* combine multiple defense families
  - Mini matrix of representative methods:
    - *DefNet*
    - *Global-AT / Target-AT*
    - *Certification methods*
    - *RGCN*
    - *Drop edges*
  - Bottom note: *Most defense work still centres on node classification*
- **Layout / UI plan:** Top half split into two concept cards: Detection/Certification and Hybrid. Bottom half contains a compact representative matrix.
- **Visual:** Small shield with magnifying glass for detection; stacked shield icons for hybrid.
- **Speaker notes:** “This is the slide where I would emphasise the paper’s overall defense-side diagnosis. There are promising directions, but the field is narrower than the attack field. A lot of methods focus on node classification, and much less has been done for broader graph tasks. Certification is especially worth highlighting for this audience: it gives a more formal notion of robustness than ‘my accuracy looked better in one experiment’.”
- **Avoid:** The full original Table III or a wall of acronyms.

### Metrics and close

The final block should reflect the paper’s unusual decision to devote a full section to metrics and a full discussion section to open problems. The goal here is not to define every metric, but to show the paper’s evaluation logic: effectiveness, efficiency, imperceptibility, then unresolved research questions on attack realism, defense breadth and efficiency, certification, and metric design itself. citeturn7view9turn8view5turn8view6turn7view10turn8view7turn8view8turn9view0turn9view1turn7view11

**Slide 19 — Why metrics deserve their own section**

- **Time:** 2.0 min
- **Purpose:** Make the metrics section feel motivated rather than administrative.
- **Visible content:**
  - *Three questions*
    - *Does it work?*
    - *What did it cost?*
    - *Can anyone notice?*
  - Bottom mapping:
    - *classification:* Acc / F1 / FNR / FPR
    - *ranking / link prediction:* AUC / AP / MRR / Hits@K
    - *clustering / community:* NMI / ARI / Modularity
- **Layout / UI plan:** Three large cards across the top. Thin task-to-metric strip below.
- **Visual:** Question-mark icons plus a small ruler icon for measurement.
- **Speaker notes:** “I like that this paper gives metrics a dedicated section, because survey talks often treat evaluation as bookkeeping. Here the authors are saying something stronger: metric choice shapes what kind of robustness claims we can make. So instead of a list, present the metrics as answers to three questions: effectiveness, efficiency, and imperceptibility.”
- **Avoid:** Reading down a bullet list of every metric from Section 5.

**Slide 20 — The few metrics worth remembering**

- **Time:** 2.5 min
- **Purpose:** Show the most presentation-worthy formulas from the metrics section.
- **Visible content:**
  - `ASR = successful attacks / attacks`
  - `AML = modified links / attacks`
  - `ADR = ASR_with_defense / ASR_without_defense − 1`
  - Small side callout:
    - *CM:* margin to the correct class
    - *Λ:* one way to assess imperceptibility
- **Layout / UI plan:** Three equal metric cards across the slide for ASR, AML, ADR. Smaller side or bottom callout for CM and `Λ`.
- **Visual:** Purple-accent metric cards with tiny one-line English gloss beneath each formula.
- **Speaker notes:** “If I only keep a few formulas from the metrics section, I’d keep these. ASR is the most intuitive effectiveness measure for attacks. AML tells us something about efficiency or perturbation cost. ADR is the defense-side summary measure that the paper explicitly mentions in the introduction. Then I’d briefly mention CM and the graph-similarity statistic as examples of task-specific or imperceptibility-aware evaluation, but I would not drown the room in all of Section 5.”
- **Avoid:** All metric formulas from the paper on one slide.

**Slide 21 — Open problems for attacks**

- **Time:** 2.0 min
- **Purpose:** Present the attack-side research agenda from the paper’s discussion section.
- **Visible content:**
  - *Unnoticeable attacks*
  - *Scalable attacks on large graphs*
  - *Weaker attacker knowledge assumptions*
  - *Real-world attacks beyond simple static graphs*
- **Layout / UI plan:** Four equal question cards with one icon and one line each.
- **Visual:** Use slightly muted attack colour so it reads as “future work”, not “active attack”.
- **Speaker notes:** “The paper’s open-problem section is useful because it distils the limitations into a research agenda. I’d phrase it this way: benchmark attacks are not the same as realistic attacks. The difficult frontier is being effective while remaining hidden, scalable, and practical under weak knowledge and more realistic graph settings.”
- **Avoid:** Bringing in a long external literature update from after the survey.

**Slide 22 — Open problems for defenses and evaluation**

- **Time:** 2.0 min
- **Purpose:** Show that the paper treats defense and metric design as still-open research areas.
- **Visible content:**
  - Left column:
    - *Defense beyond node classification*
    - *Efficient defense at scale*
    - *Certification of robustness*
  - Right column:
    - *Better cost metrics*
    - *Better imperceptibility metrics*
    - *Better metric selection by scenario*
- **Layout / UI plan:** Two-column layout: defense on the left, evaluation on the right.
- **Visual:** Shield icons on the left, ruler/gauge icons on the right.
- **Speaker notes:** “One nice feature of the paper is that it does not only say ‘we need better attacks and better defenses’. It also says evaluation itself is underdeveloped. That’s a valuable message for a technical class. If the cost of adding an edge and removing one are different, then counting modified links may be too crude. Likewise, imperceptibility on graphs is genuinely harder to define than `ℓ_p` constraints in images.”
- **Avoid:** Offering detailed new metric proposals not discussed by the paper.

**Slide 23 — What the paper leaves us with**

- **Time:** 1.7 min
- **Purpose:** Deliver a strong conclusion that reflects the paper’s contribution rather than a generic ending.
- **Visible content:**
  - *This survey’s main contribution is structure*
  - Three takeaways:
    - *Attacks are constrained perturbation problems on graphs*
    - *Defenses intervene at the data, model, objective, or monitoring level*
    - *Metrics and assumptions matter as much as raw performance*
  - Bottom line: *Think in pairs: unified attack ↔ unified defense*
- **Layout / UI plan:** Three takeaway cards in the middle. Bottom arrow pair linking attack and defense.
- **Visual:** Balanced warm-to-cool gradient only in the arrow pair, with the rest staying mostly neutral.
- **Speaker notes:** “I would end by reframing the paper’s value one last time. The main contribution is not a single best attack or a single best defense. It is a structured language for thinking about graph adversarial learning. Once you have that language, the literature becomes much easier to compare, critique, and extend.”
- **Avoid:** A generic “Thanks for listening” with no academic content.

**Slide 24 — Closing screen**

- **Time:** 0.5–1.0 min
- **Purpose:** Give yourself a clean landing slide and a small timing buffer.
- **Visible content:**
  - *A Survey of Adversarial Learning on Graphs*
  - *Reliable graph learning needs better models and better threat models*
  - Your name
- **Layout / UI plan:** Large centred title. Small toy graph in the lower-right corner. No other content.
- **Visual:** Minimal closing composition with the recurring graph motif.
- **Speaker notes:** “That’s all I want to cover. If there is one short question, I’d leave this slide up. If there is no question, this also works as a clean stopping point with a little timing slack built in.”
- **Avoid:** New technical content or a final bibliography dump.

## Formula plan

The formulas below are the ones worth showing because they clarify the survey’s framing rather than just decorating the slides. The paper’s core mathematical contribution is the move from many paper-specific formulations to a few unified ones for task learning, attack, and defense, plus a handful of evaluation metrics. citeturn7view1turn7view2turn10view1turn10view2turn7view6turn8view5turn8view6

### Generic graph learning objective

- **Where it appears:** Slide 5.
- **Why it is worth showing:** It gives the baseline supervised learning objective that the later attack and defense formulations build on.
- **How to explain it briefly:** “This is just the usual average loss over labelled training nodes. Later, attacks will try to increase the loss on targets, and defenses will try to keep performance stable despite perturbations.”
- **How to visually annotate it:** Highlight `V_L` as the labelled set, `f_θ(G,X)` as the graph model, and `y_i` as the correct label.
- **Show fully or simplified:** **Simplified full form**. Do not add task-specific variants for links and whole graphs; mention those verbally.

### Unified attack formulation

- **Where it appears:** Slide 7.
- **Why it is worth showing:** This is the paper’s central formal move on the attack side.
- **How to explain it briefly:** “The attacker chooses a perturbed graph within an allowed perturbation space and tries to maximise the loss on target instances. The inner line reminds us that the model parameters come from training.”
- **How to visually annotate it:** Use attack colour for `Ĝ`, `Ψ(G)`, and the outer `maximise`. Use a side annotation reading:
  - *control:* `Ĝ`
  - *targets:* `T`
  - *goal:* larger loss
  - *inner problem:* training
- **Show fully or simplified:** **Show full-ish version**, but abbreviate repeated notation if needed.

### Similarity or imperceptibility constraint

- **Where it appears:** Same slide as the unified attack formulation, in a bottom callout.
- **Why it is worth showing:** It formalises the idea that successful attacks should not be obviously visible.
- **How to explain it briefly:** “The perturbed graph should stay close enough to the clean graph under some similarity measure.”
- **How to visually annotate it:** Put `Q(Ĝ, G)` in a small badge labelled *how visible is the attack?*
- **Show fully or simplified:** **Simplified**. The audience only needs the concept, not a full discussion of all possible `Q`.

### Poisoning versus evasion

- **Where it appears:** Slide 10.
- **Why it is worth showing:** This is one of the cleanest places where the maths and the pipeline tell the same story.
- **How to explain it briefly:** “Poisoning changes what the model is trained on. Evasion leaves the training fixed and attacks only at test time.”
- **How to visually annotate it:** Do not show both full equations. Show only the changed training term:
  - *Poisoning:* train on `Ĝ`
  - *Evasion:* train on clean `G`
- **Show fully or simplified:** **Simplified side-by-side difference only**.

### Topology, feature, and hybrid attack constraints

- **Where it appears:** Slide 11.
- **Why it is worth showing:** These constraints translate taxonomy into concrete optimisation constraints.
- **How to explain it briefly:** “The objective stays the same, but the feasible perturbations differ: edge changes only, feature changes only, or both.”
- **How to visually annotate it:** Put the three constraints in three mini-cards:
  - *Topology:* `Σ |A − A'| ≤ Δ`
  - *Feature:* `Σ |X − X'| ≤ Δ`
  - *Hybrid:* both together
- **Show fully or simplified:** **Show constraints only**, not the full repeated maximisation objective three times.

### Unified defense formulation

- **Where it appears:** Slide 14.
- **Why it is worth showing:** It makes the defense side structurally parallel to the attack side.
- **How to explain it briefly:** “The defender wants the model’s loss to stay low on clean or attacked graphs.”
- **How to visually annotate it:** Use defense colour for `\tilde f`, `\tilde L`, and the outer `minimise`. Add one note: *same setting, opposite goal*.
- **Show fully or simplified:** **Show mildly simplified full form**.

### Metrics formulas worth keeping

- **Where they appear:** Slide 20.
- **Why they are worth showing:** They make the evaluation section concrete without overwhelming the room.
- **How to explain them briefly:**
  - `ASR`: “How often did the attack succeed?”
  - `AML`: “How many links had to be changed on average?”
  - `ADR`: “How much did the defense reduce attack success?”
- **How to visually annotate them:** Put one English sentence under each formula; that will matter more than the symbols.
- **Show fully or simplified:** **Show full simple forms** for ASR, AML, and ADR.

### Optional metric formulas

- **Where they appear:** Small callout on Slide 20 if space allows.
- **Candidates:** `CM` and the graph similarity statistic `Λ`.
- **Why they are worth showing:** `CM` is intuitive for classification; `Λ` is useful if you want one mathematical example of graph imperceptibility.
- **How to explain briefly:** “CM measures how far the wrong class beats the true class. `Λ` is one way to test whether the attacked graph still resembles the original one statistically.”
- **How to visually annotate it:** Tiny side callout only. Do not make it the main event.
- **Show fully or simplified:** `CM` can be shown fully. `Λ` should be **optional and small**.

## Table compression plan

The survey’s original tables are valuable as references, but they are not presentation-native. Table I is a notation glossary, Table II is a large attack comparison, and Table III is a large defense comparison. For a projector talk, you should compress them aggressively and make them do conceptual work rather than archival work. citeturn5view0turn11view0turn11view1

### What should be shown

Show only three compressed table-like artefacts in the entire deck:

- a **notation strip** derived from Table I,
- a **representative attack matrix** derived from Table II,
- a **representative defense matrix** derived from Table III.

That is enough to signal that the survey is broad, while keeping the deck readable.

### Notation compression

For the notation material, keep only:

- `G=(V,E)`
- `A`
- `X`
- `t`
- `Δ`
- `Ψ(G)`
- `Q`
- `f_θ`, `\hat f`, `\tilde f`

Merge or remove everything else. The audience does not need every symbol from the paper’s notation table on a slide. They only need the ones that reappear in your formulas.

### Attack table compression

For the attack summary slide, keep only these columns:

- **Method**
- **Family**
- **Task**
- **Perturbation**
- **Why it matters**

Remove or merge:

- full target-model lists,
- full baseline lists,
- full dataset lists,
- long metric lists.

Use at most **six representative rows**. A good spread is:

- Nettack
- Meta-Self / Meta-Train
- PGD / Min-Max
- RL-S2V
- IGA
- ReWatt

This spans node, link, and graph settings, and it spans greedy/gradient, optimisation, and reinforcement learning styles. The point of the slide is not completeness; it is coverage.

### Defense table compression

For the defense summary slide, keep only:

- **Method**
- **Defense type**
- **Main idea**
- **Task focus**
- **Why it matters**

Again, remove full baselines and long dataset lists. Use about **five representative rows**:

- Drop edges
- RGCN or AGCN
- VAT/BVAT or GraphDefense
- certification-based method
- DefNet or Global-AT / Target-AT

This lets the audience see preprocessing, structure, adversarial training, certification/detection, and hybrid approaches in one glance.

### Matrix versus grouped cards

Use a **matrix** when you want direct comparison across methods. Use **grouped cards** when the purpose is conceptual understanding.

For attacks and defenses, the best compromise is:

- **taxonomy slides:** grouped cards,
- **method-summary slides:** compact matrices.

### How to signal incompleteness honestly

At the bottom of both summary slides, include a one-line footer:

- *Representative examples only — see the survey tables for the fuller comparison.*

That line is important. It tells the lecturer you are intentionally compressing, not accidentally omitting.

### Highlighting representative methods

Use one visual highlight rule only:

- bold one historically important row,
- outline one row from a different task family,
- leave the rest standard.

For example:
- highlight **Nettack** on the attack slide,
- highlight **certification** or **DefNet** on the defense slide.

That prevents the matrix from looking like a spreadsheet.

## Toy example plan

The paper’s opening figure already gives you the best teaching device in the deck: a target node whose label changes after a tiny perturbation. The paper also uses a second figure to distinguish poisoning from evasion. Your deck should unify these two ideas into one recurring toy example that reappears in different sections. citeturn5view0turn10view0turn10view1

### The graph itself

Use a **small six-node graph**:

- one **target node** in the middle-right or centre,
- two or three **influencer nodes** that the attacker can leverage,
- two neutral context nodes,
- sparse enough that edge changes are immediately visible.

### Clean prediction

In the clean version:

- the target is correctly classified,
- one class colour is attached to the target prediction chip,
- the graph looks visually ordinary,
- node features are shown as tiny 3-cell or 4-cell mini-badges beside nodes.

Do not make the graph too dense. The point is legibility.

### Perturbation

Use two perturbation modes that can be turned on separately or together:

- **Topology perturbation:** add one or two edges connected to influencer nodes or rewire one target-adjacent edge.
- **Feature perturbation:** flip one or two tiny feature cells near the target or an influencer.

Then create a **hybrid version** with both visible together.

### Changed prediction

After perturbation:

- the prediction chip for the target changes colour,
- optionally add a short text label such as *clean → wrong class*,
- the target node itself should stay in the same place so the audience sees that the *graph changed*, not the *diagram*.

### What this example should teach across slides

Use the same toy graph to explain:

- **attack goal:** misclassify a target node,
- **attacker knowledge:** what information the attacker would need,
- **poisoning vs evasion:** whether the perturbation is injected before or after training,
- **topology vs feature attack:** edge changes versus feature changes,
- **hybrid attack:** both together,
- **imperceptibility:** keep only a few changes and discuss why rewiring may look less suspicious,
- **defense intuition:** remove suspicious edges, smooth messages, or train for robustness.

### Visual design of the recurring example

Keep the visual language fixed:

- target node = dark ring,
- benign nodes = neutral fill,
- class colours = blue / rose / teal,
- attack overlays = coral,
- defense overlays = teal shields or pruning marks.

On later slides, reuse the same graph at smaller scale as a corner anchor. That way the audience feels that the talk keeps returning to one running example rather than producing new pictures on every slide.

### Where to reuse it

- Slide 2: motivation
- Slide 6: standalone intuition
- Slide 10: poisoning versus evasion
- Slide 11: topology / feature / hybrid
- Slide 14: defense formulation comparison
- Slide 16: preprocessing visual
- Slide 20: metrics examples if needed

That recurrence is one of the best ways to keep a dense survey talk coherent.

## Delivery plan

### Timing summary

| Section | Slides included | Total time | Purpose |
|---|---:|---:|---|
| Opening and setup | 1–6 | 10.5 min | Motivate the topic, explain the survey’s agenda, establish notation, tasks, and the recurring toy example |
| Attack formulation and taxonomy | 7–11 | 11.0 min | Formalise attack, then organise the attack design space |
| Attack methods and limits | 12–13 | 5.0 min | Show representative methods without dumping the full survey table, then close with limitations |
| Defense formulation and taxonomy | 14–18 | 10.5 min | Mirror the attack section and make the symmetry memorable |
| Metrics | 19–20 | 4.5 min | Explain how the paper evaluates attacks and defenses beyond raw accuracy |
| Open problems | 21–22 | 4.0 min | Present the research agenda from the paper’s discussion section |
| Conclusion and slack | 23–24 | 2.5–3.5 min | Deliver takeaways and keep a small natural buffer |

Total speaking time comes out to about **44 minutes**, with roughly **1 minute of slack** depending on pacing.

### Content compression strategy

The survey is broad enough that the main failure mode is turning the talk into a bibliography recital. The way to avoid that is to compress by **decision rule**, not by random omission.

First, preserve the paper’s taxonomy by repeatedly answering the same questions. On the attack side: what does the attacker know, want, control, and optimise? On the defense side: where does the defense intervene — data, model, objective, training, or monitoring? That makes attacks and defenses symmetric enough to remember. citeturn7view3turn10view0turn10view1turn10view2turn7view7turn10view4turn10view5

Second, avoid listing every cited method. Instead, choose **representative anchors** that span task level and algorithm family. Mention the rest only as “the full table shows many more examples”. That keeps visible slides clean while still signalling breadth. The paper’s own tables support this approach because they are organised by method characteristics rather than by narrative sequence. citeturn11view0turn11view1

Third, make attacks and defenses deliberately parallel in your delivery. Show both via:
- a unified optimisation view,
- a taxonomy map,
- a representative-method summary,
- a limitations slide.

That symmetry is not accidental; it is already built into the paper’s structure, and it makes the talk much easier to follow. citeturn5view0turn7view2turn7view6turn6view4turn6view5

Fourth, keep the metrics section alive by turning it into **three evaluation questions** rather than a definition dump. The paper’s own organisation into effectiveness, efficiency, and imperceptibility supports that move directly. citeturn7view9turn8view5turn9view1

Finally, handle limitations and open questions with restraint. The visible slides should remain mostly aligned with the paper’s framing. If you want to add critique, do it in speaker notes as short comments such as:
- “This taxonomy is useful, but some boundaries overlap.”
- “Many results still live on small benchmark graphs.”
- “Metric standardisation is still weak.”

That keeps the visible deck faithful while still sounding thoughtful and mature.

### Final quality checklist

Use this after the actual slide build is done.

- **Flow**
  - Does the presentation still follow the paper’s order closely?
  - Does each major block clearly correspond to a paper section?
  - Is the attack block mirrored by the defense block?

- **Readability**
  - Can every slide be understood in under 10 seconds of first glance?
  - Is there no wall of text anywhere?
  - Are all fonts safely readable on a projector?

- **Visual support**
  - Does every dense concept have a visual companion?
  - Do formulas sit inside annotated formula cards?
  - Does the recurring toy graph appear often enough to anchor the talk?

- **Attack/defense distinction**
  - Are attack and defense instantly distinguishable by colour and iconography?
  - Are red/orange and teal/green roles used consistently throughout?

- **Formulas**
  - Is every shown formula genuinely necessary?
  - Does every formula have a plain-English explanation nearby?
  - Have you simplified repeated equations where possible?

- **Tables**
  - Are the survey tables redesigned rather than pasted?
  - Do compressed matrices have at most 5–6 columns and 5–6 rows?
  - Is there a clear note that they are representative rather than exhaustive?

- **Timing**
  - If you rehearse at normal speed, do you finish in 43–45 minutes?
  - Is there about 1 minute of natural slack without a forced Q&A block?
  - Are the heaviest slides assigned enough time?

- **Paper fidelity**
  - Would the lecturer recognise that you read the paper rather than a summary?
  - Do you preserve the survey’s wording distinctions where they matter?
  - Are visible claims aligned with the paper, with extra critique reserved for notes?

- **Understanding**
  - Would a classmate be able to explain the difference between poisoning and evasion after your talk?
  - Would they remember the attack taxonomy axes?
  - Would they understand the defense categories and why metrics matter?

- **Aesthetic finish**
  - Do all slides share the same title placement, spacing, graph style, and card style?
  - Is the final deck clean enough to feel deliberate, not improvised?
  - Does the closing slide leave a strong final impression rather than fading out?

# RAW OCR OF THE PAPER

PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 1
A Survey of Adversarial Learning on Graphs
Liang Chen, Jintang Li, Jiaying Peng, Tao Xie,
Zengxu Cao, Kun Xu, Xiangnan He, Zibin Zheng, Bingzhe Wu
Abstract—Deep learning models on graphs have achieved remarkable performance in various graph analysis tasks, e.g., node
classification, link prediction, and graph clustering. However, they expose uncertainty and unreliability against the well-designed inputs,
i.e., adversarial examples. Accordingly, a line of studies has emerged for both attack and defense addressed in different graph analysis
tasks, leading to the arms race in graph adversarial learning. Despite the booming works, there still lacks a unified problem definition
and a comprehensive review. To bridge this gap, we investigate and summarize the existing works on graph adversarial learning tasks
systemically. Specifically, we survey and unify the existing works w.r.t. attack and defense in graph analysis tasks, and give appropriate
definitions and taxonomies at the same time. Besides, we emphasize the importance of related evaluation metrics, investigate and
summarize them comprehensively. Hopefully, our works can provide a comprehensive overview and offer insights for the relevant
researchers. Latest advances in graph adversarial learning are summarized in our GitHub repository
https://github.com/EdisonLeeeee/Graph-Adversarial-Learning.
Index Terms—Adversarial Learning, Graph Neural Networks, Adversarial Attack and Defense, Adversarial Example
arXiv:2003.05730v3 [cs.LG] 5 Apr 2022
3
1 INTRODUCTION
OVER the past decade, deep learning has enjoyed the status
of crown jewels in artificial intelligence, which shows an
impressive performance in various applications, including speech
and language processing [1], [2], face recognition [3] and object
detection [4]. However, the frequently used deep learning models
recently have been proved unstable and unreliable due to the
vulnerability against perturbations. For example, slight changes on
several pixels of a picture, which appears imperceptible for human
eyes but strongly affect the outputs of deep learning models [5].
As stated by Szegedy et al. [6], deep learning models that are
well-defined and learned by backpropagation have intrinsic blind
spots and non-intuitive characteristics, which should have been
generalized to the data distribution in an obvious way.
On the other hand, deep learning on graphs has received
significant research interest recently. As a powerful representation,
graph plays an important role and has been widely applied in
real world [7]. Naturally, deep learning’s research on graph is
also a hot topic and brings lots of refreshing implementations in
different fields, such as social networks [8], e-commence networks
[9] and recommendation systems [10], [11]. Unfortunately, graph
analysis domain, a crucial field of machine learning, has also
exposed the vulnerability of deep learning models against well-
designed attacks [12], [13]. For example, consider the task of
node classification, attackers usually have control over several fake
nodes, aim to fool the target classifiers, leading to misclassification
by adding or removing edges between fake nodes and other benign
ones. As shown in Figure 1, performing small perturbations (two
added links and several changed features of nodes) on a clean
[:] [:] [:]
[:]
[:] [:] [:]
I
I
I
+ =
T
T
T
I
[:] [:]
I
I
[:] [:]
Perturbations
Prediction Prediction
[:] [:] [:]
T Target
I
I Influencer
[:] [:] [:]
I
Class1
[:]
[:]
Class2
[:] [:]
I
T
T
[:]
I
Class3
[:]
“Class 2”
[:] Node features
“Class 3”
80
92
Fig. 1: A misclassification of the target caused by a small perturbations
of the graph structure and node features.
• Liang Chen, Jintang Li, Jiaying Peng, Tao Xie, Kun Xu, and Zibin
Zheng are with Sun Yat-sen University. E-mail: {chenliang6,zhzibin}
@mail.sysu.edu.cn, {lijt55,pengjy36,xiet23}@mail2.sysu.edu.cn
• Zengxu Cao is with Hangzhou Dianzi University of China. E-mail:
czx@hdu.edu.cn
• Xiangnan He is with University of Science and Technology of China. E-
mail: xiangnanhe@gmail.com
• Bingze Wu is with Tencent AI Lab. E-mail: wubingzhe94@gmail.com
Corresponding to Liang Chen and Zibin Zheng.
graph can lead to the misclassification of deep graph learning
models.
With rising concerns being paid on the security of graph
models, there exists a surge of researches on graph adversarial
learning, i.e., a field on studying the security and vulnerability of
graph models. On one hand, from the perspective of attacking a
graph learning model, Z¨ ugner et al. [12] first study adversarial
attacks on graph data, with little perturbations on node features
and graph structure, the target classifiers are easily fooled and
misclassify specified nodes. On the other hand, Wang et al. [14]
propose a modified Graph Convolution Networks (GCNs) model
with an adversarial defense framework to improve its robustness.
Moreover, Sun et al. [15] study the existing works of adversarial
attack and defense strategies on graph data and discuss their
corresponding contributions and limitations. However, they mainly
focus on the aspect of the adversarial attack, leaving works on
defense unexplored.
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 2
Challenges. Despite a surge of works on the graph adversarial
learning, there still exists several problems to solve. i) Unified
and specified formulation. Current studies consider the problem
definition and assumptions in graph adversarial learning with
their own mathematical formulations and mostly lack of detailed
explanations, which effectively hinders the progress of follow-
up studies. ii) Related evaluation metrics. While for various
tasks, evaluation metrics on corresponding performance are rather
different, and even have diverse standardization on it. Besides,
special metrics for the graph adversarial learning scenario are
necessary and timely to explore, e.g., evaluation on the attack
impacts.
For the problem of inconsistent formulations and definitions,
we survey the existing attack and defense works, give unified def-
initions and categorize them from diverse perspectives. Although
there have been some efforts [12], [16], [17] to generalize the
definitions, most formulations still make customization for their
own models. So far, only one article [15] outlines these concepts
from a review perspective, which is not sufficient to summarize the
existing works comprehensively. Based on the previous literature,
we summarize the different types of graphs and introduce the
three main tasks according to the level, and subsequently give
the unified formulations of attack and defense in Section 3.1 and
4.1, respectively.
Different models have various metrics due to different em-
phasis. To provide guidance for researchers and better evaluate
their adversarial models, we have a more detailed summarize and
discussion on metrics in Section 5. In particular, we first introduce
some common metrics for both attack and defense, and then
present some special metrics provided in their respective works
from three categories: effectiveness, efficiency, and impercepti-
bility. For instance, the Attack Success Rate (ASR) [18] and the
Average Defense Rate (ADR) [19] are proposed to measure the
effectiveness of attack and defense, respectively.
In summary, our contributions can be listed as bellow:
• We thoroughly investigate related works in this area, and
subsequently give the unified problem formulations and
the clear definitions for current inconsistent concepts of
both attack and defense.
• We give a clear overview on existing works and classify
them from different perspectives based on reasonable
criteria systematically.
• We emphasize the importance of evaluation metrics and
investigate them to make a comprehensively summary.
• For such an emerging research area, we point out the
limitations of current researches and provide some open
questions to solve.
The survey is organized as follow. In Section 2, we will give some
basic notations of typical graphs. In Section 3 and Section 4, we
will separately introduce the definitions, taxonomies of adversarial
attack and defense on graph data, and further give a clear overview.
We then summarize the related metrics in Section 5 and try to
discuss some open research questions in Section 6. Finally, we
draw our conclusion in Section 7.
2 PRELIMINARY
Focusing on the graph structure data, we first give notations of
typical graphs for simplicity and further introduce the mainstream
tasks in graph analysis fields. The most frequently used symbols
are summarized in Table 1.
2.1 Notations
Generally, a graph is represented as G = (V,E), where
V= {v1,v2,...,vN}denotes the set of N nodes and E=
{e1,e2,...,eM}is the set of M existing edges in the graph, and
naturally E ⊆V×V. The connections of the graph could be
represented as an adjacency matrix A∈RN×N, where Ai,j ̸= 0
if there is an edge from node vi to node vj and Ai,j = 0
otherwise.
2.2 Taxonomies of Graphs
Different scenarios correspond to various types of graphs, hence
we will introduce them further in the following parts based on the
basic graph definition in Section 2.1.
Directed and Undirected Graph. Directed graph, also called a
digraph or a directed network, is a graph where all the edges are
directed from one node to another — but not backwards [20].
On the contrary, a graph where the edges are bidirectional is
called an undirected graph. For undirected graphs, the convention
for denoting the adjacency matrix doesn’t matter, as all edges
are bidirectional. Generally, Ai,j ̸= Aj,i for directed graph and
Ai,j= Aj,i for undirected graph.
Weighted and Unweighted Graph. Typically a weighted graph
refers to an edge-weighted graph where each edge is associated
with a real value [20]. An unweighted graph may be used if a rela-
tionship in terms of magnitude doesn’t exist, i.e., the connections
between edges are treated as the same.
Attributed Graph. An attributed graph refers to a graph where
both node and edge are available to have its own attributes/features
[21]. Specifically, the attributes of nodes and edges could be
denoted as Xnode ∈RN×Fnode and Xedge ∈RM×Fedge , respec-
tively. In most cases a graph usually have attributes associated
with nodes only, we use X to denote the node attributes/features
for brevity.
Homogeneous and Heterogeneous Information Graph. As well
as attributes, the type of nodes or edges is another important
property. A graph Gis called heterogeneous information graph
if there are two or more types of objects/nodes or relations/edges
in it [22], [23]; otherwise, it is called a homogeneous information
graph.
Dynamic and Static Graph. Intuitively, nodes, edges and at-
tributes are possibly changing over time in a dynamic graph [24],
which could be represented at G(t) at time t. For a static graph,
which is simply defined as G, in which nodes, edges and attributes
remain the same as the time changes.
Each type of graph has different strengths and weaknesses.
It’s better to pick the appropriate kind of graph to model the
problem. As existing works are mainly focus on a simple graph,
i.e., undirected and unweighted. Besides, they assume that the
graph is static and homogeneous for simplicity. By default, the
mentioned “graph” refers to “simple graph” in this paper.
2.3 Graph Analysis Tasks
In this section, we will introduce the major tasks of graph analysis,
in which deep learning models are commonly applied to. From the
perspective of nodes, edges and graphs, we divide these tasks into
three categories: node-, link- and graph-level task.
Node-level Task. Node classification is one of the most common
node-level tasks, for instance, identifying a person in a social
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 3
TABLE 1: Summary of notations.
Symbol Description Symbol Description Symbol Description
N number of nodes M number of edges n number of graphs
F(·)
number of features w.r.t.
nodes F(node) or edges F(edge)
˜
G a graph instance, denoting
a clean graph Gor a modified graphˆ
G C set of pre-defined class labels
for nodes, edges or graphs
V set of nodes V= {v1,v2,...,vN } E set of edges E= {e1,e2,...,eM } G set of graphs G= {G1,G2,...,Gn}
D the whole dataset,
D= (G,X,C) S set of instances, could be G, V, or E SL
set of labeled instances, could be
GL, VL, or EL, SL ⊂S
T set of unlabeled instances
where T ⊂S−SL or T= S−SL
K attackers’ knowledge of the dataset O operation set
w.r.t. attackers’ manipulation
A adjacency matrix A∈RN ×N A′ modified adjacency matrix X feature matrix
X ∈{0,1}N ×F(·) or X ∈RN ×F(·)
X′ modified feature matrix f deep learning model w.r.t. inductive
learning f(ind) or transductive learning f(tra)
ˆ
f surrogate model
˜
f well-designed model for defense θ set of parameters
w.r.t. a specific model Z output of the model
t target instance,
can be a node, an edge or a graph ∆ attack budgets y ground-truth label
w.r.t. an instance, y∈C
Ψ perturbation space
of attacks L loss function of
deep learning model Q similarity function
of graphs
network. Given a graph G, with partial labeled nodes VL ⊆Vand
other unlabeled ones, the goal of classifiers is to learn a mapping
function φ: V→C, where Cis a set of pre-defined class labels.
The learned mapping function is applied to effectively identify the
class labels for the unlabeled nodes [25]. To this end, inductive
learning and transductive learning settings are specified based on
the characteristic of training and testing procedures.
• Inductive Setting. For the inductive learning setting, a
classifier is usually trained on a set of nodes and tested
on others that never seen during training.
• Transductive Setting. Different from inductive setting, test
samples (i.e., the unlabeled nodes) can be seen (but not
their labels!) during the training procedure in transductive
learning setting.
To conclude, the objective function that optimized by the classifier
could be formulated as follows:
L=
1
|VL|vi ∈VL
L(fθ(G,X),yi) (1)
where yi is the class label of node vi, and Lcould be the loss of
either inductive learning or transductive learning, and the classifier
f with parameters θis similarly defined with the two settings.
Link-level Task. Link-level task relates to the edge classification
and link prediction. Among them, link prediction is a more
challenging task and widely used in real-world, which aims to
predict the connection strength of an edge, e.g., predicting the
potential relationship between two specified persons in a social
network, and even the new or dissolution relationship in the future.
Link prediction tasks take the same input as node classification
tasks, while the output is binary which indicates an edge will exist
or not. Therefore the objective function of link prediction tasks
could be similarly defined as Eq.(1) by changing yi ∈{0,1}, and
replacing VL with a set of labeled edges EL.
Graph-level Task. While treating the graph as a special form of
node, the graph-level tasks are similar to node-level tasks. Take the
most frequent application, graph classification, as an example, the
graph Gcould be represented as G= {G1,G2,...,Gn}, where
Gi = (Vi,Ei) is a subgraph of the entire graph. The core idea
to solve the graph classification problem is to learn a mapping
function G →C, here Crepresents the set of graph categories,
so as to predict the class for an unseen graph more accurately.
The objective function of graph classification tasks is similar with
Eq.(1) as well, in which the labeled training set is GL instead
of VL, and yi is the category of the graph Gi. In real world,
graph classification task plays an important role in many crucial
applications, such as social and biological graph classification.
3 ADVERSARIAL ATTACK
In this section, we will first introduce the definition of adversarial
attack against deep learning methods on graphs. Then, we catego-
rize these attack models from different perspectives. Finally, we
will give a clear overview on existing works.
3.1 Definition
According to existing works on graph adversarial attacks, we
summarize and give a unified formulation for them.
Attack on Graph Data. Considering f a deep learning function
designed to tackle related downstream tasks. Given a set of target
instances T ⊆S−SL, where Scould be V, Eor Grespectively
for different levels of tasks, and SL denotes the instances with
labels,1 the attacker aims to maximize the loss of the target node
on fas much as possible, resulting in the degradation of prediction
performance. Generally, we can define the attack against deep
learning models on graphs as:
maximize
G∈Ψ(G) ti ∈T
ˆ
ˆ
L(fθ∗(
Gti ,X,ti),yi)
s.t.θ∗= arg min
θ vj ∈SL
˜
L(fθ(
Gvj ,X,tj)),yj) (2)
1. Note that attackers only focus on attacking the target instances in the test
set.
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 4
ˆ
We denote a graph G∈Gwith node ti in it as Gti
.
Gdenotes
the perturbed graph and Ψ(G) indicates the perturbation space on
G, and we use˜
Gto represent original graph Gor a modified one
ˆ
G, respectively.
To make the attack as imperceptible as possible, we set a
metric for comparison between the graphs before and after the
attack, such that:
ˆ
Q(
Gti ,Gti ) <ϵ
s.t.ˆ
Gti ∈Ψ(G) (3)
where Q denotes a similarity function, and ϵ is an allowed
threshold of changes. Specifically, more metrics will be detailed
in Section 5.
3.2 Taxonomies of Attacks
As we focus on a simple graph, different types of attacks could
be conducted on the target systems. In this section, we provide
taxonomies for the attack types mainly proposed by Sun et al.
[15] and subsequently extended in our works according to various
criteria. For different scenarios, we give relevant instructions and
summarize them in the following:
3.2.1 Attacker’s Knowledge
To conduct attacks on the target system, usually an attacker will
possess certain knowledge about the target models and the dataset,
which helps them achieve the adversarial goal. Based on the
knowledge of the target models [15], we characterize different
threatening levels of attacks. White-box Attack. This is the
simplest attacks while attackers possess the entire information of
the target models, including the model architecture, parameters
and gradient information, i.e., the target models are fully exposed
to the attackers. By utilizing such rich information, attackers can
easily affect the target models and bring destructive effects. How-
ever, it is impracticable in real world since it is costly to possess
such complete knowledge of target models. Therefore white-box
attack is less dangerous but often used to approximate the worst
performance of a system under attack. Gray-box Attack. In this
case, attackers are strict to possess excessive knowledge about
the target models, this reflects real world scenarios much better
since it is more likely that attackers have limited access to get
the information, e.g., only familiar with the architecture of the
target models. Therefore, it’s harder than conducting the white-
box attack but more dangerous for the target models. Black-box
Attack. In contrast to white-box attack, black-box attack assumes
that the attacker does not know anything about the targeted
systems. Under this setting, attackers are only allowed to do black-
box queries on limited samples at most. However, it will be the
most dangerous attack once it works, since attackers can attack
any models with limited (or no) information.
Here also comes a term “no-box attack” [26] which refers
to an attack on the surrogate model based on their (limited)
understanding of the target model.2 As attackers have complete
knowledge of the surrogate model, the adversarial examples are
generated under white-box setting. No-box attack will become
a white-box attack once the attackers build a surrogate model
successfully and the adversarial examples are transferable to fool
other target models. Theoretically, this kind of attack can hardly
2. We must realize that no-box is a kind of gray- or black-box attack so we
don’t don’t have a separate category for it.
[:] [:] [:]
[:]
Model
Train
[:]
T
[:]
Original graph
Adversarial
attack
[:] [:] [:]
[:] [:]
T
[:]
Perturbed Graph
Copy
Evasion
attack
Reuse
Updated
model
Re-train
Poisoning
attack
[:] [:] [:]
[:] [:]
T
[:]
[:] [:] [:]
I
[:] [:]
T
[:]
I
[:] [:] [:]
I
[:] [:]
T
[:]
I
Fig. 2: An example of the evasion attack and the poisoning attack.
(Image Credit: Z¨ unger et al. [12])
affect the systems in most cases with these constraints. However,
as if the surrogate model has strong transferability, the no-box
attack is also destructive.
As attackers are strict with the knowledge of the target models,
they also have less access to the information of the dataset D.
Based on the different levels of knowledge of the targeted system
[27], we have: Perfect Knowledge. In this case, the dataset D,
including the entire graph structure, node features, and even the
ground-truth labels of objects, are completely exposed to attackers,
i.e., the attacker is assumed to know everything about the dataset.
This is impractical but the most common setting in previous
studies. However, considering the damage that could be done by
an attacker with perfect knowledge is critical, since it may expose
the potential weaknesses of the target system in a graph.
Moderate Knowledge. The moderate knowledge case represents
an attacker with less information about the dataset. This makes
attackers focus more on the performance of their attacks, or even
search for more information through legitimate or illegitimate
methods.
Minimal Knowledge. This is the hardest one as attackers can
only conduct attacks with the minimal knowledge of datasets,
such as partial connections of the graph or the feature information
of certain nodes. This is essential information for an attacker,
otherwise it will fail even under the white-box attack setting. The
minimal knowledge case represents the least sophisticated attacker
and naturally with less threat level.
To conclude, we use Kto denote the attackers’ knowledge
in an abstract knowledge space. Here Kis consisting of three
main parts, the dataset knowledge, the training algorithm and
the learned parameters of target models. For instance, K=
(D,f,θ) denotes white-box attack with perfect knowledge, and
ˆ
ˆ
K= (Dtrain,
f,
θ) denotes gray- or black-box attack and with
moderate knowledge, whereˆ
f andˆ
θ come from the surrogate
model and Dtrain ⊂Ddenotes the training dataset.
3.2.2 Attacker’s Goal
The goal generally distinguishes three different types of attacks,
i.e., security violation, attack specificity and error specificity [28].
They are not mutually exclusive in fact, and more details are
discussed below.
Security Violation. Security violation can be categorized into
availability attack, integrity attack and others. For availability
attack, the the attacker attempts to destroy the function of the
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 5
system, thereby impairing its normal operation. The damage is
global, that is, it attacks the overall performance of the whole
system. For integrity attack, the attackers’ purpose is to bypass
or fool the detection of the system, which is different from
availability attack in that it does not destroy the normal operation
of the system. There are other goals, such as reverse-engineering
model information to gain privacy knowledge.
Error Specificity. Take node classification task as an example, the
error specific attack aims to misclassify the predictions as specific
labels, while unspecific attack does not care what the prediction
is, the attack is considered successful as long as the prediction is
wrong.
Attack Specificity. This perspective focuses on the range of the
attack, which can divide attacks into targeted attack and non-
targeted attack (general attack). The targeted attack focuses on
a specific subset of nodes (usually a target node), while the
non-targeted attack is undifferentiated and global. With reference
to Eq.(2), the difference is the domain of T ⊂ S−SL or
T= S−SL.
It is worth noting that in some other fields (e.g., computer
vision), targeted attack refers to the specific error attack, and non-
targeted attack the unspecific error attack. In the field of graph
adversarial learning, we suggest that distinguishing the targeted
attack based on the attack range, and whether it is error specific
based on the consequence.
3.2.3 Attacker’s Capability
Attacks can be divided into poisoning attack and evasion at-
tack according to adversaries’ capabilities, which are occurred
at different stages of the attacks. Poisoning Attack. Poisoning
attacks (a.k.a training-time attacks) try to affect the performance
of the target models by modifying the dataset in the training
stage, i.e., the target models are trained on the poisoned datasets.
Since transductive learning is widely used in most graph analysis
tasks, the test samples (but not their labels) are participated in
the training stage, which leads to the popularity of poisoning
attacks. Under this scenario, the parameters of target models are
retrained after the training dataset being modified, thus we can
define poisoning attacks according to Eq.(2):
maximize
G∈Ψ(G) ti ∈T
ˆ
ˆ
L(fθ∗(
Gti ,X,ti),yi)
s.t.θ∗= arg min
θ vj ∈SL
ˆ
L(fθ(
Gvj ,X,vj),yj) (4)
Evasion Attack. While poisoning attacks focus on the training
phase, evasion attacks (a.k.a test-time attacks) tend to add adver-
sarial examples in test time. Evasion attacks occur after the target
model is well trained on a clean graph, i.e., the learned parameters
are fixed during evasion attacks. Therefore, we can define the
formulation of evasion attacks by changing part of Eq.(4) slightly:
θ∗= arg min
θ vj ∈SL
L(fθ(Gvj ,X,vj),yj) (5)
In Figure 2, we show a toy example of the poisoning attack
and the evasion attack. In most cases the poisoning attack does
not work well because the model is retrained to alleviate the
adversarial impacts.
3.2.4 Attack Strategy
For attacking a target model on graph data, attackers may have
a line of strategies to achieve their adversarial goals. In most
instances, they will focus on the graph structure or node/edge
features. Based on the strategy applied on a graph, we have:
Topology Attack. Attackers are mainly focus on the the topology
of the graph, a.k.a, structure attack. For example, they are allowed
to add or remove some edges legally between nodes in the graph to
fool the target system. To specify this, we define an attack budget
∆ ∈N, thus the definition of the topology attack is:
maximize
G∈Ψ(G) ti ∈T
ˆ
ˆ
L(fθ∗(
Gti ,X,ti),yi)
(6)
s.t.
|Au,v−A′
u,v|≤∆
u<v
where A′is the adjacency matrix of the perturbed graph, and θ∗
is discussed in Section 3.2.3.
Feature Attack. Although the topology attack is more common,
attackers can conduct feature attacks as well. Under this setting,
the features of specified objects will be changed. However, unlike
graph structure, the node/edge features could be either binary or
continuous, i.e., X ∈{0,1}N×F(·) or X ∈RN×F(·) . For binary
features, attackers can flip them like edges, while for continuous
features, attackers can add a small value on them, respectively.
Thus the definition of feature attacks is:
maximize
G∈Ψ(G) ti ∈T
ˆ
ˆ
L(fθ∗(
Gti ,X,ti),yi)
(7)
s.t.
u j
|Xu,j−X′
u,j|≤∆
where X′is similarly defined, and here ∆ ∈N for binary features
and ∆ ∈R for continuous features.
Hybrid. Usually, attackers will conduct both attack strategies
at the same time to exert more powerful impact. Besides, they
could even add several fake nodes (with fake labels), which
will have their own features and relationship with other benign
instances. For example, some fake users will be added into the
recommendation system and affect the results of the system [29],
[30]. Therefore, we conclude a unified formulation as follows:
maximize
G∈Ψ(G) ti ∈T
ˆ
ˆ
L(fθ∗(
Gti ,X,ti),yi)
(8)
s.t.
|Au,v−A′
u,v|+
u<v
u j
|Xu,j−X′
u,j|≤∆
A′ and X′ may not have the same dimension with A and X
respectively if some fake nodes are added into the graph.
3.2.5 Attacker’s Manipulation
Although attackers may have enough knowledge about the target
system, they may not always have access to manipulation all of
the dataset. Besides, different manipulations may have different
budget cost. For example, in an e-commerce system [31], attack-
ers could only purchase more items (add edges) but unable to
delete the purchase records (remove edges). Based on different
manipulation, we have: Add. In a graph, attackers could add edges
between different nodes, or add features on specified nodes/edges.
This is the most simplest manipulation and naturally has lowest
budget in most scenarios. Remove. In a graph, attackers could
remove edges between different nodes, or remove features on
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 6
specified nodes/edges. This kind of manipulation will be harder
than “add”, since attackers may not have enough access to execute
the “remove” manipulation. Rewiring. The manipulations men-
tioned above may become more noticeable for the target system
if ∆ is larger. To address this problem, the rewiring operation is
proposed in a less noticeable way than simple adding/removing
manipulation [16], [32]. For instance, attackers can add an edge
connected with a target node, while remove an edge connected
with it at the same time. Each time of rewiring manipulation
related to two single operations, which can preserve some basic
graph properties (e.g., degree) and naturally more unnoticeable.
To conclude, we define an operation set O=
{OAdd,ORem,ORew}, representing the above three manipula-
tions of attackers, respectively.
3.2.6 Attack Algorithm
Generally speaking, current methods of adversarial attacks on
generating adversarial examples are mainly based on the gradient
information, either from the target model (white-box attack) or the
surrogate model (black- or gray-box attack). Beyond that, there are
several methods generating adversarial examples based on other
algorithms. From the perspective of attack algorithm, we have:
Gradient-based Algorithm. Intuitively, gradient-based algorithm
is simple but effective. The core idea is that: fix the parameters
of a trained model, and regard the input as a hyperparameter
to optimize. Similar to the training process, attackers could use
the partial derivative of loss Lwith respect to edges (topology
attack) or features (feature attack), to decide how to manipulate
the dataset. However, gradients could not applied directly into
the input data due to the discreteness of the graph data, instead,
attackers often choose the one with greatest absolute gradients,
and manipulate it with a proper value. While most deep learning
models are optimized by gradients, on the contrary, attackers could
destroy them by gradients as well.
Non-gradient-based Algorithm. In addition to gradient infor-
mation, attackers could generate adversarial examples in other
ways. For example, from the perspective of the genetic algorithm,
attackers can choose the population (adversarial examples) with
highest fitness score (e.g., erroneous outputs of the target/surrogate
model) generations by generations. Besides, reinforcement learn-
ing algorithms are also commonly used to solve this issue. Re-
inforcement learning based attack methods [16], [17] will learn
the generalizable adversarial examples within an action space.
Moreover, adversarial examples can even generated by a well-
designed generative model.
3.2.7 Target Task
As discussed in Section 2.3, there exists three major tasks in
graph domains. According to different levels of tasks, we can
divide existing attack methods into the following three categories,
respectively.
Node-relevant Task. Currently, there are several attack models
against node-relevant tasks [12], [17], [17], [18], [32], [33],
[34], [35], [36], [37], [38], [39], [40], [41], [42], [43]. Typically,
Bojchevski et al. and Hou et al. [30], [33] utilize random walk [44]
as an surrogate model to attack node embedding, Dai et al. [17]
uses a reinforcement learning based framework to disturb node
classification tasks. In general, most of the existing works address
in node classification task due to its ubiquity in real world.
Link-relevant Task. Many relationships in real world can be
represented by graph. For some of these graphs, such as social
graph, are always dynamic in reality. Therefore, the link prediction
on the graph comes into being, in order to predict the change of
the edge. Link prediction is also the most common application of
link-relevant tasks and there are many attack related studies have
been proposed [18], [29], [32], [41], [42], [42], [45], [46].
Graph-relevant Task. Graph-relevant tasks treat graph as a basic
unit. Compared to node- or link-relevant tasks, it is macro and
large-scale. The application of graph-relevant methods are more
inclined to the research community of biology, chemistry, envi-
ronment, materials, etc. In this task, the model tries to extract
features of nodes and spatial structures to represent a graph, so
as to achieve downstream operations such as graph classification
or clustering. Similar with Eq.(2), the targets of attack should be
an graphs, while y is determined by the specific task. For graph-
relevant tasks, some attack researches have also appeared [16],
[27], [47].
3.3 Summary: Attack on Graph
In this part, we will discuss the main contributions of current
works, and point out the limitations to be overcome, and propose
several open questions in this area. Specifically, we cover these
released papers and its characteristic in Table 2.
3.3.1 Major Contributions
So far, most of the existing works in the attack scenario are mainly
based on the gradients, either the adjacency matrix or feature
matrix, leading to topology attack and feature attack, respectively.
However, the gradients’ information of the target model is hard to
acquire, instead, attackers will train a surrogate model to extract
the gradients. In addition to gradient-based algorithms, several
heuristic methods are proposed to achieve the goal of attack,
such as genetic algorithm [51] and reinforcement learning [52]
based algorithms. According to different tasks in graph analysis,
we summarize the major contributions of current works in the
following.
Node-relevant Task. Most of the researches focus on the node
classification task. The work [12] is the first to study the ad-
versarial attack on graph data, using an efficient greedy search
method to perform perturbations on node features and graph
structure and attacking traditional graph learning model. From the
perspective of gradients, there are several works [17], [34], [35],
[36], [37], [43] focus on the topology attack, adding/removing
edges between nodes based on the gradients information form
various surrogate models. Specially, Xu et al. [34] present a
novel optimized-based attack method that uses the gradients of
surrogate model and facilitates the difficulty of tackling discrete
graph data; Z¨ ugner et al. [35] use meta-gradients to solve the
bilevel problem of poisoning a graph; Wang et al. [36] propose a
greedy method based on Generative Adversarial Network (GAN)
[53] to generate adjacency and feature matrices of fake nodes,
which will be injected to a graph to misclassify the target models;
Chen et al. and Dai et al. [17], [37] both use GCN as a surrogate
model to extract gradients information and thus generating an
adversarial graph; Wu et al. [43] argue that integrated gradients
can better reflect the effect of perturbing certain features or edges.
Moreover, Dai et al. [17] consider evasion attacks on the task
of node classification and graph classification, and proposes two
effective attack methods based on the reinforcement learning and
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 7
TABLE 2: Related works on attack in details.
Reference Model Algorithm Target Task Target Model Baseline Metric Dataset
[48] GF-Attack Graph signal processing Node classification GCN, SGC,
DeepWalk, LINE
Random,
Degree,
RL-S2V,
Aclass
Accuracy
Cora,
Citeseer,
Pubmed
[43] IG-FGSM,
IG-JSMA Gradient-based GCN Node classification GCN
FGSM,
JSMA,
Nettack
Classification margin,
Accuracy
Cora,
Citeseer,
PolBlogs
[49] EPA Genetic algorithm Community detection GRE, INF,
LOU
AQ, AS , AB ,
AD , DS , DW
NMI,
ARI
Synthetic networks,
Football, Email,
Polblogs
[35] Meta-Self,
Meta-Train Gradient-Based GCN Node classification
GCN,
CLN,
Deepwalk
DICE,
Nettack,
First-order
Misclassification rate,
Accuracy
Cora-ML,
Citeseer,
PolBlogs,
PubMed,
[33] ADW 2,
ADW 3
Gradient-based random walk Node classification,
Link prediction Deepwalk
Brnd
Beig
Bdeg
F1 score,
Classification margin
Cora,
Citeseer,
PolBlogs
[46] TGA-Tra,
TGA-Gre Gradient-based DDNE Link prediction
DDNE,
ctRBM,
GTRBM,
dynAERNN
Random,
DGA,
CNA
ASR, AML
RADOSLAW,
LKML,
FB-WOSN
[16] ReWatt Reinforcement learning
based on GCN
Graph
classification GCN RL-S2V,
Random ASR
REDDIT-
MULTI-12K,
REDDIT-MULTI-5K,
IMDB-MULTI
[34] PGD,
Min-Max Gradient-based GCN Node classification GCN
DICE,
Meta-Self,
Greedy
Misclassification
rate
Cora,
Citeseer
[38] EDA Genetic algorithm
based on Deepwalk
Node classification,
Community detection
HOPE,
LPA,
EM,
Deepwalk
Random,
DICE,
RLS,
DBA
NMI,
Micro-F1,
Macro-F1
Karate,
Game,
Dolphin
[39] DAGAER Generative model based
on VGAE Node classification GCN Nettack ASR Cora,
Citeseer
[50] - Knowledge embedding Fact plausibility
prediction
TransE,
TransR,
RESCAL
Random MRR, HR@K FB15k,
WN18
[40] - Based on LinLBP Node classification,
Evasion
LinLBP, JW, GCN
LBP, RW, LINE
DeepWalk
Node2vec
Random,
Nettack
FNR,
FPR
Facebook, Enron,
Epinions,
Twitter,
Google+
[47] Q-Attack Genetic algorithm Community detection
FN, Lou, SOA,
LPA, INF,
Node2vec+KM
Random,
CDA,
DBA
NMI,
Modularity Q
Karate,
Dolphins,
Football,
Polbooks,
[30] HG-attack Label propagation algorithm,
Nodes injection Malware detection Orig-HGC AN-Attack TP, TN, FP, FN, F1,
Precision, Recall, Accuracy
Tencent Security
Lab Dataset
[29] UNAttack Gradient-based similarity method,
Nodes injection Recommendation Memory-based CF,
BPRMF, NCF
Random,
Average,
Popular,
Co-visitation
Hit@K
Filmtrust,
Movielens,
Amazon
[45] -
Gradient-based GAN and MF,
Nodes injection Recommendation MF -
Attack difference,
TVD, JS, Est.,
Rank loss @K,
Adversarial loss
MovieLens 100k,
MovieLens 1M
[36] Greedy GAN Gradient-based GCN and GAN Node
classification GCN Random Accuracy,
F1 score, ASR
Cora,
Citeseer
[32] CTR, OTC Neighbor score based
on graph structure Link prediction
Traditional
link prediction
algorithms
- AUC, AP
WTC 9/11,
ScaleFree,
Facebook,
Random network
[18] IGA Gradient-based GAE Link prediction
GAE,LRW
DeepWalk,
Node2vec,
CN, Random, Katz
RAN,
DICE,
GA
ASR,
AML
NS,
Yeast,
FaceBook
[17] RL-S2V Reinforcement learning Node/Graph
Classification
GCN,
GNN
Random
sampling Accuracy
Citeseer, Cora,
Finance,
Pubmed
[12] Nettack Greedy search & gradient
based on GCN Node classification
GCN,
CLN,
Deepwalk
Rnd,
FGSM
Classification margin,
Accuracy,
Cora-ML,
Citeseer,
PolBlogs
[37] FGA Gradient-based GCN Node classification,
Community detection
GCN, GraRep,
DeepWalk,
Node2vec,
LINE, GraphGAN
Random,
DICE,
Nettack
ASR, AML
Cora,
Citeseer,
PolBlogs,
[41] Opt-attack Gradient-based Deepwalk and Link prediction
DeepWalk,
LINE, SC
Node2vec, GAE
Random,
PageRank,
Degree sum,
Shortest path
AP,
Similarity Score
Facebook,
Cora,
Citeseer
[42] Approx-Local Similarity methods Link prediction
Local& global
similarity
metrics
RandomDel,
GreedyBase
Katz similarity,
ACT distance,
Similarity score
Random network,
Facebook
[27] Targeted noise injection,
Small community attack Noise injection Graph clustering,
Community detection
SVD, Node2vec,
Community
detection algorithms
- ASR, FPR
Reverse,
Engineered,
DGA,
Domains,
NXDOMAIN
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 8
genetic algorithms, respectively. Taking Deepwalk [44] as a base
method, Bojchevski et al. [33] and Xuan et al. [38] propose
a eigen decomposition and genetic algorithm based strategy to
attack the network embedding, respectively. Also, Bose et al. [39]
design a unified encoder-decoder framework from the generative
perspective, which can be employed to attack diverse domains
(images, text and graphs), Wang et al. [40] propose a threat model
to manipulate the graph structure to evade detection by solving
a graph-based optimization problem efficiently. Considering real-
world application scenarios, Hou et al. [30] propose an algorithm
that allows malware to evade detection by injecting nodes (apps).
Link-relevant Task. Link prediction is another fundamental re-
search problems in network analysis. In this scenario, Waniek et al.
[32] study the link connections, and propose heuristic algorithms
to evade the detection by rewiring operations. Furthermore, Chen
et al. [18] put forward a novel iterative gradient attack method
based on a graph auto-encoder framework. Similarly, Chen et al.
[46] also exploit the gradients information of surrogate model,
and firstly study the works about adversarial attacks on dynamic
network link prediction (DNLP). Besides, Sun et al. [41] focus on
poisoning attacks and propose a unified optimization framework
based on projected gradient descent. In the recommendation sce-
nario, considering the interactions between users and items as a
graph and treat it as a link prediction task, Christakopoulou et al.
[45] and Chen et al. [29] propose the method of injecting fake
users to degrade the recommendation performance of the system.
Graph-relevant Task. Few works study the adversarial attacks
on this scenario, Ma et al. [16] propose a rewiring operation based
algorithm, which uses reinforcement learning to learn the attack
strategy on the task of graph classification. Besides, Chen et al.
[47] introduce the problem of community detection and proposes
a genetic algorithm based method. Chen et al. [27] focus on graph
clustering and community detection scenarios, devise generic
attack algorithms based on noise injection and demonstrates their
effectiveness against a real-world system.
Unlike conducting attacks on ideal datasets, this brings
more challenges to attackers.
4 DEFENSE
The proposed attack methods have made researchers realize the
importance of the robustness of deep learning models. Relatively,
some defense methods have also been proposed. In this section,
we will give some general definitions of defense models against
adversarial attack methods on graph data and its related concepts.
In addition, this section systematically classifies existing defense
methods and details some typical defense algorithms.
4.1 Definition
Simply put, the purpose of defense is to make the performance
of the model still maintain a certain stability on the data that is
maliciously disturbed. Although some defense models have been
proposed, there is no clear and unified definition of the defense
problem. To facilitate the discussion of the following, we propose
a unified formulation of the defense problem. Defense on Graph
Data. Most symbols are the same as mentioned in Section 3, and
we define˜
f as a deep learning function with the loss function˜
L
designed for defense, it receives a graph either perturbed or not.
Then the defense problem can be defined as:
minimize
G∈Ψ(G)∪Gti ∈T
˜
˜
ˆ
ˆ
L(
fθ∗(
Gti ,X,ti),yi)
s.t.θ∗= arg min
θ vj ∈SL
˜
˜
˜
L(
fθ(
Gvj ,X,vj),yj) (9)
where˜
G∈Ψ(G) ∪Gcan be a well-designed graphˆ
Gfor the
purpose of defense, or a clean graph G, which depends on whether
the model have been attacked.
4.2 Taxonomies of Defenses
3.3.2 Current Limitations
Despite the remarkable achievements on attacking graph learning
models, there are several limitations remain to be overcome:
• Unnoticeability. Most works are unaware of preserving
the adversarial attacks from noticeable impacts, they sim-
ply consider the lower attack budgets but far from enough
instead.
• Scalability. Existing works are mainly focus on a rela-
tively small-scale graph, however, million-scale or even
larger graphs are commonly seen in real life, and efficient
attacks on larger graph are leaving unexplored.3
• Knowledge. It is common to assume that attackers have
perfect knowledge about the dataset, but it is unreasonable
and impractical due to the limited access of attackers. Nev-
ertheless, very few works conduct attacks with moderate
or even minimal knowledge.
• Physical Attack. Most of the existing works conduct
attacks on ideal datasets. However, in real world, attacks
need to consider more factors. For instance, in a physical
attack the adversarial examples as input will be distorted
accidentally and it often fails to achieve the desired results.
3. There has been some efforts on large-scale graph computation that would
be useful for graph learning methods. [54], [55]
In this section, we divide the existing defense methods into several
categories according to the used algorithms and describe them by
examples. To the best of our knowledge, it’s the first time for those
defense methods to be clearly classified and the first time for those
types to be clearly defined. All taxonomies are listed below:
Preprocessing-based Defense. As the most intuitive way, directly
manipulating the raw data has a great impact on the model
performance. Additionally, preprocessing raw data is independent
to model structures and training methods, which gives consid-
erable scalability and transferability. Some existing works [43]
improve model robustness by conducting certain preprocessing
steps before training, and we define this type of defense methods
as Preprocessing-based Defense. In addition, Wu et al. [43] try to
drop edges that connect nodes with low similarity score, which
could reduce the risk for those edges of being attack and nearly
does no harm to the model performance.
Structure-based Defense. In addition to raw data, model structure
is also crucial to the model performance. Some existing works
modify the model structure, such as GCN, to gain more robustness,
and we define this type of defense methods as Structure-based
Defense. Instead of GCN’s graph convolutional layers, Zhu et
al. [56] use Gaussian-based graph convolutional layers, which
learns node embeddings from Gaussian distributions and assign
attention weight according to their variances. Wang et al. [14]
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 9
propose dual-stage aggregation as a Graph Neural Network (GNN)
encoder layer to learn the information of neighborhoods, and
adopt GAN [53] to conduct contrastive learning. Tang et al.
[57] initialize the model by meta-optimization and penalize the
aggregation process of GNN. And Ioannidis et al. [58] propose
a novel GCN architecture, named Adaptive Graph Convolutional
Network (AGCN), to conduct robust semi-supervised learning.
Adversarial-based Defense. Adversarial training has been widely
used in deep learning due to its excellent performance. Some
researchers successfully adopt adversarial training from other
fields into graph domain to improve model robustness, and we
define the defense methods which use adversarial training as
Adversarial-based Defense. There are two types of adversarial
training: i) Training with adversarial goals. Some adversarial
training methods gradually optimize the model in a continuous
min-max way, under the guide of two opposite (minimize and
maximize) objective functions [34], [59], [60]; ii) Training with
adversarial examples. Other adversarial-based models are fed with
adversarial samples during training, which helps the model learn to
adjust to adversarial samples and thus reduces the negative impacts
of those potential attack samples [19], [61], [62], [63].
Objective-based Defense. As a simple and effective method,
modifying objective function plays an important role in improving
the model robustness. Many existing works attempt to train a ro-
bust model against adversarial attacks by optimizing the objective
function, and we define this type of defense methods as Objective-
based Defense. However, there is a little intersection between the
definition of Objective-based Defense and Adversarial-based De-
fense mentioned above, because the min-max adversarial training
(the first type of Adversarial-based Defense) is also in the range
of objective optimization. Therefore, to accurately distinguish
the definition boundary between Adversarial-based Defense and
Objective-based Defense, we only consider those methods which
are objective-based but not adversarial-based as the instances of
Objective-based Defense. Z¨ ugner et al. [13] and Bojchevski et al.
[64] combine hinge loss and cross entropy loss to perform a robust
optimization. Jin et al. [65] and Chen et al. [19] regularize the
training process by studying the characteristics of graph powering
and smoothing the cross-entropy loss function, respectively.
Detection-based Defense. Some existing works focus on the
detection of adversarial attacks, or the certification of model/node
robustness, which we define as Detection-based Defense. Al-
though those detection-based methods are unable to improve the
model robustness directly, they can serve as supervisors who keep
monitoring the model security and alarm for awareness when an
attack is detected. Z¨ ugner et al. [13] and Bojchevski et al. [64]
propose novel methods to certificate whether a node is robust, and
a robust node means it won’t be affected even under the worse-
case/strongest attack. Pezeshkpour et al. [66] study the impacts of
adding/removing edges by performing adversarial modifications
on the graph. Xu et al. [67] adopt link prediction and its variants
to detect the potential risks, and for example, link with low score
could be a maliciously added edge. Zhang et al. [68] utilize
perturbations to explore the model structure and propose a method
to detect adversarial attack. Hou et al. [30] detect the target node
by uncovering the poisoning nodes injected in the heterogeneous
graph [69]. Ioannidis et al. [70] effectively detect anomalous nodes
in large-scale graphs by applying a graph-based random sampling
and consensus strategies.
Hybrid Defense. As the name suggested, we define Hybrid De-
fense to denote the defense method which consists of two or more
types of different defense algorithms mentioned above. Many
researches flexibly combine several types of defense algorithms
to achieve better performance, thus alleviate the limitations of
only using a single method. As mentioned above, Z¨ ugner et al.
[13] and Bojchevski et al. [64] address the certification problem
of node robustness and conduct robust training with objective-
based optimization. Wang et al. [14] focus on improving the
model structure and adversarially train the model by GAN. Chen
et al. [19] adopt adversarial training and other regularization
mechanisms (e.g., gradient smoothing, loss smoothing). Xu et al.
[67] propose a novel graph generation method together with other
detection mechanisms (e.g., link prediction, subgraph sampling,
outlier detect) as preprocessing to detect potential malicious edges.
Miller et al. [71] consider a combination of the features come from
graph structure and origin node attributes and use well-designed
training data selection methods to do a classification task. These
are instances of the hybrid defense.
Others. Currently, the amount of researches for defense is far
less than that of attack on the graph domain. To the best of our
knowledge, most existing works for defense only focus on node
classification tasks, and there are a lot of opportunities to study
defense methods with different tasks on graph, which will enrich
our defense types. For example, Pezeshkpour et al. [66] evaluate
the robustness of several link prediction models and Zhou et al.
[72] adopt the heuristic approach to reduce the damage of attacks.
4.3 Summary: Defense on Graph
In this section, we will introduce the contributions and limitations
of current works about defense. Then, we will discuss the potential
research opportunities in this area. The details and comparisons of
various methods are placed in Table 3.
4.3.1 Major Contributions
Currently, most of the methods to improve the robustness of
GNNs start from two aspects: a robust training method or a
robust model structure. Among them, the training methods are
mostly adversarial training, and many of the model structure im-
provements are made using the attention mechanism. In addition,
there are some studies that do not directly improve the robustness
of GNNs but try to verify the robustness or try to detect the
data that is disturbed. In this part, considering the different ways
in which existing methods contribute to the adversarial defense
of graphs, we summarize the contributions of graph defense
from the following three perspectives: adversarial learning, model
improvement and others. Adversarial Learning. As a successful
method that has shown to be effective in defending the adversarial
attacks of image data and test data, adversarial learning [73]
augments the training data with adversarial examples during the
training stage. Some researchers have also tried to apply this
kind of idea to graph defense methods. Wang et al. [14] think
the vulnerabilities of graph neural networks are related to the
aggregation layer and the perceptron layer. To address these two
disadvantages, they propose an adversarial training framework
with a modified GNN model to improve the robustness of GNNs.
Chen et al. [19] propose different defense strategies based on
adversarial training for target and global adversarial attack with
smoothing distillation and smoothing cross-entropy loss function.
Feng et al. [60] propose a method of adversarial training for
the attack on node features with a graph adversarial regularizer
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 10
TABLE 3: Related works on defense in details. The type is divided according to the algorithm.
Reference Model Algorithm Type Target Task Target Model Baseline Metric Dataset
[13] GNN (trained with
RH-U)
Robustness certification,
Objective based Hybrid Node
classification
GNN,
GCN
GNN
(trained with
CE, RCE, RH)
Accuracy,
Averaged
Worst-case
Margin
Citeseer,
Cora-ML,
Pubmed
[34] - Adversarial training Adversarial
training
Node
classification GCN GCN Accuracy,
Misclassification rate
Citeseer,
Cora
[65] r-GCN,
VPN
Graph
powering
Objective
based
Node
classification GCN
ManiReg,
ICA,
Vanilla GCN,
...
Accuracy, Robustness merit,
Attack deterioration
Citeseer,
Cora,
Pubmed
[43] - Drop edges Preprocessing Node
classification GCN GCN Accuracy,
Classification margin
Citeseer,
Cora-ML,
Polblogs
[14] DefNet
GAN,
GER,
ACL
Hybrid Node
classification
GCN,
GraphSAGE
GCN,
GraphSAGE
Classification
margin
Citeseer,
Cora,
Polblogs
[66] CRIAGE Adversarial
modification
Robustness
evaluation
Link
prediction
Knowledge
graph
embeddings
-
Hits@K,
MRR
Nations,
Kinship,
WN18,
YAGO3-10
[56] RGCN Gaussian-based
GCN
Structure
based
Node
classification GCN GCN,
GAT Accuracy
Citeseer,
Cora,
Pubmed
[19]
Global-AT,
Target-AT,
SD, SCEL
Adversarial
training,
Smooth defense
Hybrid Node
classification GNN AT ADR,
ACD
Citeseer,
Cora,
PolBlogs
[59] SVAT,
DVAT VAT Adversarial
training
Node
classification GCN GCN Accuracy
Citeseer,
Cora,
Pubmed
[68] -
KL
divergence
Detection
based
Node
classification
GCN,
GAT
-
Classification margin,
Accuracy, ROC, AUC
Citeseer,
Cora,
PolBlogs
[60] GCN-GATV GAT,
VAT
Adversarial
training
Node
classification GCN
DeepWalk,
GCN,
GraphSGAN,
...
Accuracy
Citeseer,
Cora,
NELL
[62] S-BVAT,
O-BVAT BVAT Adversarial
training
Node
classification GCN
ManiReg,
GAT,
GPNN,
GCN,
VAT,
...
Accuracy
Citeseer,
Cora,
Pubmed,
NELL
[57] PA-GNN Penalized aggregation,
Meta learning
Structure
based
Node
classification GNN
GCN,
GAT,
PreProcess,
RGCN,
VPN
Accuracy
Pubmed,
Reddit,
Yelp-Small,
Yelp-Large
[61] GraphDefense Adversarial
training
Adversarial
training
Node/Graph
classification GCN Drop edges,
Discrete AT Accuracy
Cora,
Citeseer,
Reddit
[30] HG-HGC HG-Defense Detection
based Malware detection
Malware
detection
system
Other malware
detection systems Detection rate Tencent Security
Lab Dataset
[58] AGCN Adaptive GCN with
edge dithering
Structure
based
Node
classification GCN GCN Accuracy
Citeseer,
PolBlogs,
Cora, Pubmed
[70] GraphSAC Random sampling,
Consensus
Detection
based
Anomaly
detection
Anomaly
model
GAE,
Degree,
Cut ratio,
...
AUC
Citeseer,
PolBlogs,
Cora, Pubmed
[64] GNN (train with
LRCE , LCEM )
Robustness certification,
Objective based Hybrid Node
classification GNN GNN
Accuracy,
Worst-case
Margin
Cora-ML,
Citeseer,
Pubmed
[72] IDOpt,
IDRank
Integer Program,
Edge Ranking
Heuristic
algorithm
Link
prediction
Similarity-based
link prediction
models
PPN DPR
PA,
PLD,
TVShow,
Gov
[71]
SVM with
a radial basis
function kernel
Augmented feature,
Edge selecting Hybrid Node
classification SVM GCN Classification
marigin
Cora,
Citeseer
[63] APR,
AMF
MF-BPR
based AT
Adversarial
training Recommendation MF-BPR
ItemPop,
MF-BPR,
CDAE,
NeuMF,
IRGAN
HR,
NDCG
Yelp,
Pinterest,
Gowalla
[67]
SL, OD,
P+GGD,
ENS,GGD
Link prediction,
Subsampling,
Neighbour analysis
Hybrid Node
classification GNN, GCN LP AUC Citeseer,
Cora
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS which encourages the model to generate similar predictions on
the perturbed target node and its connected nodes. Sun et al.
[59] successfully transfer the efficiency of Virtual Adversarial
Training (VAT) to the semi-supervised node classification task on
graphs and applies some regularization mechanisms on original
GCN to refine its generalization performance. Wang et al. [61]
point out that the values of perturbation in adversarial training
could be continuous or even negative. And they propose an
adversarial training method to improve the robustness of GCN.
He et al. [63] adopt adversarial training to Bayesian Personalized
Ranking (BPR) [74] on recommendation by adding adversarial
perturbations on embedding vectors of the user and item. Model
Improvement. In addition to improvements in training methods,
many studies have focused on improving the model itself. In recent
years, the attention mechanism [75] has shown extraordinary
performance in the field of natural language processing. Some
studies of graph defense have borrowed the way that they can
automatically give weight to different features to reduce the
influence of perturbed edges on features. Zhu et al. [56] use
Gaussian distributions to absorb the effects of adversarial attacks
and introduce a variance-based attention mechanism to prevent
the propagation of adversarial attacks. Tang et al. [57] propose
a novel framework base on a penalized aggregation mechanism
which restrict the negative impact of adversarial edges. Hou et
al. [30] enhance the robustness of malware detection system in
Android by their well-designed defense mechanism to uncover
the possible injected poisoning nodes. Jin et al. [65] point out the
basic flaws of the Laplacian operator in origin GCN and propose
a variable power operator to alleviate the issues. Miller et al. [71]
propose to use unsupervised methods to extract the features of
the graph structure and use support vector machines to complete
the task of node classification. In addition, they also propose two
new training data partitioning strategies. Others. In addition to
improving the robustness of the model, there are also some studies
that have made other contributions around robustness, such as
detecting disturbed edges, certificating node robustness, analyses
of current attack methods and so on. Z¨ ugner et al. [13] propose the
first work on certifying the robustness of GNNs. The method can
give robustness certification which states whether a node is robust
under a certain space of perturbations. Zhang et al. [68] study the
defense methods’ performance under random attacks and Nettack
concluded that graph defense models which use structure explo-
ration are more robust in general. Otherwise, this paper proposes
a method to detect the perturbed edges by calculating the mean of
the KL divergences [76] between the softmax probabilities of the
node and it’s neighbors. Pezeshkpour et al. [66] introduce a novel
method to automatically detect the error for knowledge graphs
by conducting adversarial modifications on knowledge graphs. In
addition, the method can study the interpretability of knowledge
graph representations by summarizing the most influential facts
for each relation. Wu et al. [43] argue that the robustness issue is
rooted in the local aggregation in GCN by analyzing attacks on
GCN and propose an effective defense method based on prepro-
cessing. Bojchevski et al. [64] propose a robustness certificate
method that can certificate the robustness of GNNs regarding
perturbations of the graph structure and the label propagation. In
addition, they also propose a new robust training method guided by
their own certificate method. Zhou et al. [72] model the problem
of robust link prediction as a Bayesian Stackelberg game [77]
and propose two defense strategies to choose which link should
11
be protected. Ioannidis et al. [58] propose a novel edge-dithering
(ED) approach reconstructs the original neighborhood structure
with high probability as the number of sampled graphs increases.
Ioannidis et al. [70] introduce a graph-based random sampling
and consensus approach to effectively detect anomalous nodes in
large-scale graphs.
4.3.2 Current Limitations
As a new-rising branch that has not been sufficiently studied,
current defense methods have several major limitations as follows:
• Diversity. At present, most works of defense mainly focus
on node classification tasks only. From the perspective of
defender, they need to improve their model robustness on
different tasks.
• Scalability. Whether a defense model can be widely used
in practice largely depends on the cost of model training.
Most existing works lack the consideration of training
costs.
• Theoretical Proof. Most of current methods only illustrate
their effectiveness by showing experimental results and
textual descriptions. It will be great if a new robust
method’s effectiveness can be proved theoretically.
5 METRICS
In this section, we first introduce the metrics that are common
in graph analysis tasks, which are used in attack and defense
scenarios as well. Next, we introduce some new metrics proposed
in attack and defense works from three perspectives: effectiveness,
efficiency, and imperceptibility.
5.1 Common Metrics
• FNR and FPR. In the classification or clustering tasks,
here is a category of metrics based on False Positive (FP),
False Negative (FN), True Positive (TP) and True Negative
(TN). In attack and defense scenarios, commonly used to
quantify are False Negative Rate (FNR) and False Positive
Rate (FPR). Specifically, FNR is equal to FN over (TP
+ FN), and FPR is equal to FP over (FP + TN). For all
negative samples, the former describes the proportion of
false positive samples detected, while the latter describes
the proportion of false negative samples detected. In other
words, for negative samples, the former is the error rate,
and the latter is the miss rate.
• Accuracy (Acc). The Accuracy is one of the most com-
monly used evaluation metrics, which measures the quality
of results based on the percentage of correct predictions
over total instances.
• F1-score. The F1 score [33] can be regarded as a harmonic
average of model Precision and Recall score [78], with a
maximum value of 1 and a minimum value of 0.
• Area Under Curve (AUC). The AUC is the area under
the Receiver Operating Characteristic (ROC) curve [68].
Different models corresponding to different ROC curves,
and it is difficult to compare which one is better if
there is a crossover between the curves, thus comparison
based on the AUC score is more reasonable. In general,
AUC indicates the probability that the predicted positive
examples rank in front of the negative examples.
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS • Average Precision (AP). As the area under the Precision-
Recall curve, AP is described as one of the most robust
metrics [79]. Precision-Recall curve depicts the relation-
ships between Precision and Recall. A good model should
improve the Recall while preserving the Precision a rel-
atively high score. In contrast, weaker models may lose
more Precision in order to improve Recall. Comparing
with the Precision-Recall curve, AP can show the perfor-
mance of the model more intuitively.
• Mean Reciprocal Rank (MRR). The MRR is a com-
monly used metric to measure a rank model. For a target
query, if the first correct item is ranked nth, then the MRR
score is 1/n, and once there is no match, the score is 0.
The MRR of the model is the sum of the scores of all
queries.
• Hits@K. By calculating the rank (e.g., MRR) of all the
ground-truth triples, Hits@K is the proportion of correct
entities ranked in top K.
• Modularity. The Modularity is an important measure
based on the assortative mixing [80], which usually used
to assess the quality of different division for a particular
network, especially the community structure is unknown
[81].
• Normalized Mutual Information (NMI). The NMI is
another commonly used evaluation to measure the quality
of clustering results, so as to analyze the network com-
munity structure [82]. NMI further indicates the similarity
between two partitions with mutual information and in-
formation entropy, while a larger value means a higher
similarity.
• Adjusted Rand Index (ARI). The ARI is a measure of
the similarity between two data clusterings: one given by
the clustering process and the other defined by external
criteria [83]. Such a correction establishes a baseline by
using the expected similarity of all pair-wise comparisons
between clusterings specified by a random model. ARI
measures the relation between pairs of dataset elements
without labels’ information, which can cooperate with
conventional performance measures to detect classification
algorithm. In addition, ARI can also use labels information
for feature selection [83].
5.2 Specific Metrics for Attack and Defense
In order to measure the performance, a number of specific metrics
for attack and defense appear in literature. Next, we will organize
these metrics from three perspectives: effectiveness, efficiency,
and imperceptibility.
5.2.1 Effectiveness-relevant Metrics
Both attack and defense require metrics to measure the perfor-
mance of the target model before and after the attack. Therefore,
we have summarized some metrics for measuring effectiveness
and list them below:
• Attack Success Rate (ASR). ASR is the ratio of targets
which will be successfully attacked within a given fixed
budget [18]. Correspondingly, we can conclude the for-
mulation of ASR:
ASR=
Number of successful attacks
Number of attacks (10)
12
• Classification Margin (CM). CM is only designed for the
classification task. Under this scenario, attackers aim to
perturbe a graph that misclassifies the target node and has
maximal “distance” (in terms of log-probabilities/logits)
to the correct class [12]. Based on this, CM is well
formulated as:
CM = max
Zt,y′
t
−Zt,yt (11)
y′
t ̸=yt
where Zt is the output of the target model with respect to
node t, and yt ∈Cis the correct class label of vt while y′
t
is the wrong one.
• Averaged Worst-case Margin (AWM). Worst-case Mar-
gin (WM) is the minimum of the Classification Margin
(CM) [13], and the average of WM is dynamically calcu-
lated over a mini-batch of nodes during training. The Bs
in the following equation denotes batch size.
AWM=
1
Bs
i=Bs
CMworsti (12)
i=1
• Robustness Merit (RM). It evaluates the robustness of
the model by calculating the difference between the post-
attack accuracy and pre-attack accuracy on GNNs [65].
And Vattacked denotes the set of nodes theoretically affected
by the attack.
RM= Accpost-attacked
Vattacked−Accpre-attacked
Vattacked (13)
• Attack Deterioration (AD). It evaluates the attack effect
of the model prediction. Note that any added/dropped
edges can only affect the nodes within the spatial scope in
the origin network [65], due to the spatial scope limitaions
of the GNNs.
Accpost-attacked
AD = 1−
Vattacked
(14)
Accpre-attacked
Vattacked
• Average Defense Rate (ADR). ADR is the ratio of the
difference between the ASR of attack on GNNs with
and without defense, versus the ASR of attack on GNNs
without defense [19]. The higher ADR the better defense
performance.
ASRwith-defense
ADR=
Vattacked
−1 (15)
ASRwithout-defense
Vattacked
• Average Confidence Different (ACD). ACD is the av-
erage confidence different of nodes in Ns before and
after attack [19], where Ns is the set of nodes which
are classified correctly before attack in test set. Note that
Confidence Different (CD) is equivalent to Classification
Margin (CM).
1
ACD=
Ns vi ∈Ns
ˆ
CDi(
Avi )−CDi(A) (16)
• Damage Prevention Ratio (DPR). Damage prevention
is defined to measure the amount of damage that can be
prevented by defense [72]. Let L0 be the defender’s loss
without attack, LA be the defender’s loss under a certain
attack strategy, A and LD be the defender’s loss with a
certain defense strategy D. A better defense strategy leads
to a larger DPR.
LA−LD
LA−L0
(17)
DPRD
A =
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS 5.2.2 Efficiency-relevant Metrics
Here we introduce some efficiency metrics which measure the cost
of the attack and defense. For example, the metric of quantifying
how much perturbations are required for the same effect.
• Average Modified Links (AML). AML is designed for
the topology attack, which indicates the average perturba-
tion size leading to a successful attack [18]. Assume that
attackers have limited budgets to attack a target model,
the modified links (added or removed) are accumulated
until attackers achieve their goal or run out of the budgets.
Based on this, we can conclude the formulation of AML:
Number of modified links
AML=
Number of attacks (18)
5.2.3 Imperceptibility-relevant Metrics
Several metrics are proposed to measure the scale of the manip-
ulations caused by attack and defense, which are summarized as
follows:
• Similarity Score. Generally speaking, Similarity Score
is a measure to infer the likelihoods of the existence of
links, which usually applied in the link-level task [42],
[84]. Specifically, suppose we want to figure out whether
a particular link (u,v) exists in a network, Similarity
Score can be used to quantify the topology properties of
node u and v (e.g., common neighbors, degrees), and a
higher Similarity Score indicates a greater likelihood of
connection between this pair. Usually, Similarity Score
could be measured by the cosine similarity matrix [41].
• Test Statistic Λ. Λ takes advantage of the distribution of
node degrees to measure the similarity between graphs.
Specifically, Z¨ ugner et al. [12] state that multiset of node
degrees dG in the graph G follow the power-law like
distribution, and they provide a method to approximate the
main parameter αG of the distribution. Through αG and
dG, we can calculate G’s log-likelihood score l(dG,αG).
For the pre-attack graph Gpr and post-attack graph Gpo,
we get (dGpr ,αGpr ) and (dGpo ,αGpo ), respectively. Simi-
larly, we can then define dGq
= dGpr
∩dGpo
and estimate
αGq . The final test statistic of graphs can be formulated
as:
Λ(Gpr,Gpo) = 2·(−l(dGq ,αGq )
+ l(dGpo ,αGpo ) + l(dGpr ,αGpr )) (19)
Finally, when the statistic Λ satisfies a specified constraint,
the model considers the perturbations are unnoticeable.
• Attack Budget ∆. To ensure unnoticeable perturbations in
the attack, previous work [12] measures the perturbations
in terms of the budget ∆ and the test statistics Λ w.r.t.
log-likelihood score. More precisely, they accumulate the
changes in node feature and the adjacency matrix, and
limit it to a budge ∆ to constrain perturbations. However,
it is not suitable to deal with complicated situations [12].
• Attack Effect. Generally, the attack effect evaluates the
impacts in the community detection task. Given a con-
fusion matrix J, where each element Ji,j represents the
number of shared nodes between original community and
a perturbed one, the attack effect is simply defined as the
accumulation of normalized entropy [49]. Suppose all the
communities keep exactly the same after the attack, the
attack effect will be equal to 0.
13
6 OPEN PROBLEMS
Graph adversarial learning has many problems worth to be stud-
ied by observing existing researches. In this section, we try to
introduce several major research issues and discuss the potential
solutions. Generally, we will discuss the open problems in three
parts: attack, defense and evaluation metric.
6.1 Attack
We mainly approach the problems from three perspectives, at-
tacks’ side effects, performance, and prerequisites. First, we hope
the inevitable disturbances in the attack can be stealthy and
unnoticeable. Second, now that data is huge, attacks need to be
efficient and scalable. Finally, the premise of the attack should not
be too ideal, that is, it should be practical and feasible. Based on
the limitations of previous works detailed in Section 3.3.2 and the
discussion above, we rise several open problems in the following:
• Unnoticeable Attack. Adversaries want to keep the attack
unnoticeable to avoid censorship. To this end, Z¨
ugner
et al. [35] argue that the main property of the graph
should be marginally changed after attack, e.g., attackers
are restricted to maintain the degree distribution while
attacking a specified graph, which is evaluated via a test
static. Nevertheless, most of existing works ignore such a
constraint despite achieving outstanding performance. To
be more concealed, we believe that attackers should focus
more on their perturbation impacts on a target graph, with
more constraints placed on the attacks.
• Efficient and Effective Algorithms. Seeing from Ta-
ble 2, the most frequently used benchmark datasets are
rather small-scale graphs, e.g., Cora [85] and Citeseer
[86]. Currently, the majority of proposed methods are
failed to attack a large-scale graph, for the reason that
they need to store the entire information of the graph
to compute the surrogate gradients or loss even with
small changes, leading to the expensive computation and
memory consumption. To address this problem, Z¨
ugner
et al. [35] make an effort that derives an incremental
update for all candidate set (potential perturbation edges)
with a linear variant of GCN, which avoid the redundant
computation while remain efficient attack performance.
Unfortunately, the proposed method isn’t suitable for a
larger-scale graph yet. With the shortcoming that unable
to conduct attacks on a larger-scale graph, a more efficient
and effective attack method should be studied to address
this practical problem. For instance, given a target node,
the message propagation are only exits within its k-hops
neighborhood.4 In other words, we believe that adversaries
can explore a heuristic method to attack an entire graph
(large) via its represented subgraph (small), and naturally
the complexity of time and space are reduced.
• Constraints on Attackers’ Knowledge. To conduct a real
and practical black-box attack, attackers should not only
be blind to the model knowledge, but also be strict to min-
imal data knowledge. This is a challenging setting from
the perspective of attackers. Chen et al. [27] explore this
setting by randomly sampling different size of subgraphs,
showing that the attacks are failed with a small network
4. Here k depends on the specified method of message propagation and is
usually of a smaller value, e.g., k= 2 with a two-layer GCN.
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS size, and the performance increases as it gets larger. How-
ever, few works are aware of the constraints on attackers’
knowledge, instead, they assume that perfect knowledge
of the input data are available, and naturally perform well
in attacking a fully “exposed” graph. Therefore, several
works could be explored with such a strict constraint, e.g.,
attackers can train a substitute model on a certain part of
the graph, learn the general patterns of conducting attacks
on graph data, thus transfer to other models and entire
graph with less prior knowledge.
• Real-world Attack. Attacks can’t always be on an ideal
assumption, i.e., studying attacks on a simple and static
graphs. Such ideal, undistorted input is unrealistic in
real cases. In other words, how can we improve existing
models so that they can work in complex real-world
environments?
6.2 Defense
Besides the open problems of attack mentioned above, there are
still many interesting problems in defense on the graph, which
deserve more attentions. Here we list some open problems that
worth discussing:
• Defense on Various Tasks. From table 3 we can see
that, most existing works of defense [13], [14], [34],
[43], [65] are focusing on the node classification task on
graph, achieving promising performance. Except for node
classification, there are various tasks on graph domain are
important and should be pay more attention to. However,
only a few works [66], [72] try to investigate and improve
model robustness on link prediction task on graph while
a few works [30], [63], [70] make an effort to defense on
some tasks (e.g., malware detection, anomaly detection,
recommendation) on other graph domains. Therefore, it is
valuable to think about how to improve model robustness
on various tasks or transfer the current defense methods to
other tasks.
• Efficient Defense. Training cost is critical important factor
to be taken into consideration under the industrial scenes.
Therefore, it’s worth to be studied how to guarantee
acceptable cost while improving robustness. However, the
currently proposed defense methods have rarely discussed
the space-time efficiency of their algorithms. Wang et al.
[14] design a bottleneck mapping to reduce the dimension
of input for a better efficiency, but their experiments
absence the consideration of large-scale graph. Z¨ ugner et
al. [13] test the number of coverage iterations of their
certification methods under the different number of nodes,
but the datasets they used are still small. Wang et al.
[61] do not restrict the regularized adjacency matrix to
be discrete during the training process, which improves
the training efficiency.
• Certification on Robustness. Robustness of the graph
model is always the main issue among all the existing
works including attack and defense mentioned above.
However, most researchers only focus on improving model
(e.g., GCN) robustness, and try to prove the model ro-
bustness via the performance results of their model. The
experimental results can indeed prove the robustness of
the model to a certain extent. However, considering that
14
the model performance is easily influenced by the hyper-
parameters, implementation method, random initialization,
and even some hardware constraints (e.g., cpu, gpu, mem-
ory), it is difficult to guarantee that the promising and sta-
ble performance can be reobtained on different scenarios
(e.g., datasets, tasks, parameter settings). There is a novel
and cheaper way to prove robustness via certification that
should be taken more seriously into consideration, which
certificate the node’s absolute robustness under arbitrary
perturbations, but currently only a few works have paid
attention to the certification of GNNs’ robustness [13],
[64] which are also a valuable research direction.
6.3 Evaluation Metric
As seen in Section 5, we got so many evaluation metrics in graph
adversarial learning field, however, the number of effectiveness-
relevant metrics are far more than the other two, which reflects the
research emphasis on model performance is unbalanced. There-
fore, we propose several potential works can be further studied:
• Measurement of Cost. There are not many metrics to
explore the model’s efficiency which reflects the lack
of research attention on it. The known methods roughly
measure the cost via the number of modified edges which
begs the question that is there another perspective to
quantify the cost of attack and defense more precisely?
In real world, the cost of adding an edge is rather different
from removing one,5 thus the cost between modified edges
are unbalanced, which needs more reasonable evaluation
metrics.
• Measurement of Imperceptibility. Different from the
image data, where the perturbations are bounded in ℓp-
norm [15], [73], [87], and could be used as an evaluation
metric on attack impacts, but it is ill-defined on graph
data. Therefore, how to better measure the effect of per-
turbations and make the attack more unnoticeable?
• Appropriate Metric Selection. With so many metrics
proposed to evaluate the performance of the attack and
defense algorithms, here comes a problem that how to
determine the evaluation metrics in different scenarios?
7 CONCLUSION
In this survey, we conduct a comprehensive review on graph ad-
versarial learning, including attacks, defenses and corresponding
evaluation metrics. To the best of our knowledge, this is the first
work systemically summarize the extensive works in this field.
Specifically, we present the recent developments of this area and
introduce the arms race between attackers and defenders. Besides,
we provide a reasonable taxonomy for both of them, and further
give a unified problem formulation which makes it clear and
understandable. Moreover, under the scenario of graph adversarial
learning, we summarize and discuss the major contributions and
limitations of current attack and defense methods respectively,
along with the open problems of this area that worth exploring.
Our works cover most of the relevant evaluation metrics in the
graph adversarial learning field as well, aiming to provide a better
understanding on these methods. In the future, we will measure
the performance of proposed models with relevant metrics based
on extensive empirical studies.
5. Usually, removing an edge is more expensive than adding one.
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS Hopefully, our works will serve as a reference and give
researchers a comprehensive and systematical understanding of
the fundamental issues, thus become a well starting point to study
in this field.
REFERENCES
[1] W. Xiong, J. Droppo, X. Huang, F. Seide, M. Seltzer, A. Stolcke,
D. Yu, and G. Zweig, “Achieving human parity in conversational speech
recognition,” arXiv preprint arXiv:1610.05256, 2016.
[2] R. Collobert, J. Weston, L. Bottou, M. Karlen, K. Kavukcuoglu, and
P. Kuksa, “Natural language processing (almost) from scratch,” Journal
of machine learning research, vol. 12, no. Aug, pp. 2493–2537, 2011.
[3] O. M. Parkhi, A. Vedaldi, A. Zisserman et al., “Deep face recognition.”
in bmvc, vol. 1, no. 3, 2015, p. 6.
[4] B. Krishnamurthy and M. Sarkar, “Deep-learning network architecture
for object detection,” Dec. 11 2018, uS Patent 10,152,655.
[5] N. Papernot, P. McDaniel, I. Goodfellow, S. Jha, Z. B. Celik, and
A. Swami, “Practical black-box attacks against machine learning,” in
Proceedings of the 2017 ACM on Asia conference on computer and
communications security. ACM, 2017, pp. 506–519.
[6] C. Szegedy, W. Zaremba, I. Sutskever, J. Bruna, D. Erhan, I. Goodfellow,
and R. Fergus, “Intriguing properties of neural networks,” arXiv preprint
arXiv:1312.6199, 2013.
[7] P. Goyal and E. Ferrara, “Graph embedding techniques, applications, and
performance: A survey,” Knowledge-Based Systems, vol. 151, pp. 78–94,
2018.
[8] Y. Pei, N. Chakraborty, and K. Sycara, “Nonnegative matrix tri-
factorization with graph regularization for community detection in social
networks,” in Twenty-Fourth International Joint Conference on Artificial
Intelligence, 2015.
[9] J. Wang, P. Huang, H. Zhao, Z. Zhang, B. Zhao, and D. L. Lee,
“Billion-scale commodity embedding for e-commerce recommendation
in alibaba,” in Proceedings of the 24th ACM SIGKDD International
Conference on Knowledge Discovery & Data Mining. ACM, 2018,
pp. 839–848.
[10] L. Chen, Y. Liu, Z. Zheng, and P. Yu, “Heterogeneous neural attentive
factorization machine for rating prediction,” in CIKM. ACM, 2018, pp.
833–842.
[11] F. Xie, L. Chen, Y. Ye, Z. Zheng, and X. Lin, “Factorization machine
based service recommendation on heterogeneous information networks,”
in ICWS. IEEE, 2018, pp. 115–122.
[12] D. Z¨ ugner, A. Akbarnejad, and S. G¨ unnemann, “Adversarial attacks
on neural networks for graph data,” in Proceedings of the 24th ACM
SIGKDD International Conference on Knowledge Discovery & Data
Mining. ACM, 2018, pp. 2847–2856.
[13] D. Z¨ ugner and S. G¨ unnemann, “Certifiable robustness and robust training
for graph convolutional networks,” in Proceedings of the 25th ACM
SIGKDD International Conference on Knowledge Discovery & Data
Mining. ACM, 2019, pp. 246–256.
[14] S. Wang, Z. Chen, J. Ni, X. Yu, Z. Li, H. Chen, and P. S. Yu, “Ad-
versarial defense framework for graph neural network,” arXiv preprint
arXiv:1905.03679, 2019.
[15] L. Sun, J. Wang, P. S. Yu, and B. Li, “Adversarial attack and defense on
graph data: A survey,” arXiv preprint arXiv:1812.10528, 2018.
[16] Y. Ma, S. Wang, L. Wu, and J. Tang, “Attacking graph convolutional
networks via rewiring,” arXiv preprint arXiv:1906.03750, 2019.
[17] H. Dai, H. Li, T. Tian, X. Huang, L. Wang, J. Zhu, and L. Song, “Adver-
sarial attack on graph structured data,” arXiv preprint arXiv:1806.02371,
2018.
[18] J. Chen, Z. Shi, Y. Wu, X. Xu, and H. Zheng, “Link prediction adversarial
attack,” arXiv preprint arXiv:1810.01110, 2018.
[19] J. Chen, Y. Wu, X. Lin, and Q. Xuan, “Can adversarial network attack be
defended?” arXiv preprint arXiv:1903.05994, 2019.
[20] G. Chartrand, Introductory graph theory. Courier Corporation, 1977.
[21] K. Ding, J. Li, R. Bhanushali, and H. Liu, “Deep anomaly detection
on attributed networks,” in Proceedings of the 2019 SIAM International
Conference on Data Mining. SIAM, 2019, pp. 594–602.
[22] Z. Liu, C. Chen, X. Yang, J. Zhou, X. Li, and L. Song, “Heterogeneous
graph neural networks for malicious account detection,” in Proceedings
of the 27th ACM International Conference on Information and Knowl-
edge Management. ACM, 2018, pp. 2077–2085.
[23] R. Hussein, D. Yang, and P. Cudr´ e-Mauroux, “Are meta-paths neces-
sary?: Revisiting heterogeneous graph embeddings,” in Proceedings of
the 27th ACM International Conference on Information and Knowledge
Management. ACM, 2018, pp. 437–446.
15
[24] F. Manessi, A. Rozza, and M. Manzo, “Dynamic graph convolutional
networks,” Pattern Recognition, vol. 97, p. 107000, 2020.
[25] T. N. Kipf and M. Welling, “Semi-supervised classification with graph
convolutional networks,” in International Conference on Learning Rep-
resentations (ICLR), 2017.
[26] Y. Sharma, “Gradient-based adversarial attacks to deep neural networks
in limited access settings,” Ph.D. dissertation, COOPER UNION, 2018.
[27] Y. Chen, Y. Nadji, A. Kountouras, F. Monrose, R. Perdisci, M. An-
tonakakis, and N. Vasiloglou, “Practical attacks against graph-based
clustering,” in Proceedings of the 2017 ACM SIGSAC Conference on
Computer and Communications Security. ACM, 2017, pp. 1125–1142.
[28] B. Biggio and F. Roli, “Wild patterns: Ten years after the rise of
adversarial machine learning,” Pattern Recognition, vol. 84, pp. 317–331,
2018.
[29] L. Chen, Y. Xu, F. Xie, M. Huang, and Z. Zheng, “Data poisoning attacks
on neighborhood-based recommender systems,” 2019.
[30] S. Hou, Y. Fan, Y. Zhang, Y. Ye, J. Lei, W. Wan, J. Wang, Q. Xiong, and
F. Shao, “αcyber: Enhancing robustness of android malware detection
system against adversarial attacks on heterogeneous graph based model,”
in Proceedings of the 28th ACM International Conference on Information
and Knowledge Management. ACM, 2019, pp. 609–618.
[31] L. Chen, Y. Liu, X. He, L. Gao, and Z. Zheng, “Matching user with item
set: Collaborative bundle recommendation with deep attention network,”
in IJCAI, 2019, pp. 2095–2101.
[32] M. Waniek, K. Zhou, Y. Vorobeychik, E. Moro, T. P. Michalak, and
T. Rahwan, “Attack tolerance of link prediction algorithms: How to hide
your relations in a social network,” arXiv preprint arXiv:1809.00152,
2018.
[33] A. Bojchevski and S. G¨ unnemann, “Adversarial attacks on node em-
beddings via graph poisoning,” in International Conference on Machine
Learning, 2019, pp. 695–704.
[34] K. Xu, H. Chen, S. Liu, P.-Y. Chen, T.-W. Weng, M. Hong, and X. Lin,
“Topology attack and defense for graph neural networks: An optimization
perspective,” arXiv preprint arXiv:1906.04214, 2019.
[35] D. Z¨ ugner and S. G¨ unnemann, “Adversarial attacks on graph neural
networks via meta learning,” arXiv preprint arXiv:1902.08412, 2019.
[36] X. Wang, J. Eaton, C.-J. Hsieh, and F. Wu, “Attack graph convolutional
networks by adding fake nodes,” arXiv preprint arXiv:1810.10751, 2018.
[37] J. Chen, Y. Wu, X. Xu, Y. Chen, H. Zheng, and Q. Xuan, “Fast gradient
attack on network embedding,” arXiv preprint arXiv:1809.02797, 2018.
[38] Q. Xuan, J. Zheng, L. Chen, S. Yu, J. Chen, D. Zhang, and Q. Z. Member,
“Unsupervised euclidean distance attack on network embedding,” arXiv
preprint arXiv:1905.11015, 2019.
[39] A. J. Bose, A. Cianflone, and W. Hamiltion, “Generalizable adversar-
ial attacks using generative models,” arXiv preprint arXiv:1905.10864,
2019.
[40] B. Wang and N. Z. Gong, “Attacking graph-based classification via
manipulating the graph structure,” arXiv preprint arXiv:1903.00553,
2019.
[41] M. Sun, J. Tang, H. Li, B. Li, C. Xiao, Y. Chen, and D. Song, “Data
poisoning attack against unsupervised node embedding methods,” arXiv
preprint arXiv:1810.12881, 2018.
[42] K. Zhou, T. P. Michalak, M. Waniek, T. Rahwan, and Y. Vorobeychik,
“Attacking similarity-based link prediction in social networks,” in Pro-
ceedings of the 18th International Conference on Autonomous Agents and
MultiAgent Systems. International Foundation for Autonomous Agents
and Multiagent Systems, 2018, pp. 305–313.
[43] H. Wu, C. Wang, Y. Tyshetskiy, A. Docherty, K. Lu, and L. Zhu,
“Adversarial examples for graph data: deep insights into attack and
defense,” in Proceedings of the 28th International Joint Conference on
Artificial Intelligence. AAAI Press, 2019, pp. 4816–4823.
[44] B. Perozzi, R. Al-Rfou, and S. Skiena, “Deepwalk: Online learning of
social representations,” in KDD. ACM, 2014, pp. 701–710.
[45] K. Christakopoulou and A. Banerjee, “Adversarial recommendation:
Attack of the learned fake users,” arXiv preprint arXiv:1809.08336, 2018.
[46] J. Chen, J. Zhang, Z. Chen, M. Du, F. Li, and Q. Xuan, “Time-aware
gradient attack on dynamic network link prediction,” arXiv preprint
arXiv:1911.10561, 2019.
[47] J. Chen, L. Chen, Y. Chen, M. Zhao, S. Yu, Q. Xuan, and X. Yang,
“Ga-based q-attack on community detection,” IEEE Transactions on
Computational Social Systems, vol. 6, no. 3, pp. 491–503, 2019.
[48] H. Chang, Y. Rong, T. Xu, W. Huang, H. Zhang, P. Cui, W. Zhu,
and J. Huang, “A restricted black-box adversarial framework towards
attacking graph embedding models,” 2019.
[49] J. Chen, Y. Chen, L. Chen, M. Zhao, and Q. Xuan, “Multiscale evo-
lutionary perturbation attack on community detection,” arXiv preprint
arXiv:1910.09741, 2019.
PREPRINT: A SURVEY OF ADVERSARIAL LEARNING ON GRAPHS [50] H. Zhang, T. Zheng, J. Gao, C. Miao, L. Su, Y. Li, and K. Ren, “Data
poisoning attack against knowledge graph embedding,” in Proceedings of
the 28th International Joint Conference on Artificial Intelligence. AAAI
Press, 2019, pp. 4853–4859.
[51] D. Whitley, “A genetic algorithm tutorial,” Statistics and computing,
vol. 4, no. 2, pp. 65–85, 1994.
[52] R. S. Sutton and A. G. Barto, Reinforcement learning: An introduction.
MIT press, 2018.
[53] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley,
S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial networks,”
2014.
[54] X. Zhu, W. Chen, W. Zheng, and X. Ma, “Gemini: A computation-centric
distributed graph processing system,” in 12th {USENIX}Symposium on
Operating Systems Design and Implementation ({OSDI}16), 2016, pp.
301–316.
[55] K. Yang, M. Zhang, K. Chen, X. Ma, Y. Bai, and Y. Jiang, “Knightking:
a fast distributed graph random walk engine,” in Proceedings of the 27th
ACM Symposium on Operating Systems Principles, 2019, pp. 524–537.
[56] D. Zhu, Z. Zhang, P. Cui, and W. Zhu, “Robust graph convolutional
networks against adversarial attacks,” 2019.
[57] X. Tang, Y. Li, Y. Sun, H. Yao, P. Mitra, and S. Wang, “Robust graph
neural network against poisoning attacks via transfer learning,” arXiv
preprint arXiv:1908.07558, 2019.
[58] V. N. Ioannidis and G. B. Giannakis, “Edge dithering for robust adaptive
graph convolutional networks,” arXiv preprint arXiv:1910.09590, 2019.
[59] K. Sun, Z. Lin, H. Guo, and Z. Zhu, “Virtual adversarial training on graph
convolutional networks in node classification,” in Chinese Conference on
Pattern Recognition and Computer Vision (PRCV). Springer, 2019, pp.
431–443.
[60] F. Feng, X. He, J. Tang, and T.-S. Chua, “Graph adversarial training:
Dynamically regularizing based on graph structure,” arXiv preprint
arXiv:1902.08226, 2019.
[61] X. Wang, X. Liu, and C.-J. Hsieh, “Graphdefense: Towards robust graph
convolutional networks,” arXiv preprint arXiv:1911.04429, 2019.
[62] Z. Deng, Y. Dong, and J. Zhu, “Batch virtual adversarial training for
graph convolutional networks,” arXiv preprint arXiv:1902.09192, 2019.
[63] X. He, Z. He, X. Du, and T.-S. Chua, “Adversarial personalized ranking
for recommendation,” in The 41st International ACM SIGIR Conference
on Research & Development in Information Retrieval. ACM, 2018, pp.
355–364.
[64] A. Bojchevski and S. G¨ unnemann, “Certifiable robustness to graph
perturbations,” in Advances in Neural Information Processing Systems,
2019, pp. 8317–8328.
[65] M. Jin, H. Chang, W. Zhu, and S. Sojoudi, “Power up! robust graph
convolutional network against evasion attacks based on graph powering,”
arXiv preprint arXiv:1905.10029, 2019.
[66] P. Pezeshkpour, C. Irvine, Y. Tian, and S. Singh, “Investigating robustness
and interpretability of link prediction via adversarial modifications,” in
Proceedings of NAACL-HLT, 2019, pp. 3336–3347.
[67] X. Xu, Y. Yu, B. Li, L. Song, C. Liu, and C. Gunter, “Characterizing
malicious edges targeting on graph neural networks,” 2018.
[68] Y. Zhang, S. Khan, and M. Coates, “Comparing and detecting adversarial
attacks for graph deep learning,” in Proc. Representation Learning on
Graphs and Manifolds Workshop, Int. Conf. Learning Representations,
New Orleans, LA, USA, 2019.
[69] Y. Sun, J. Han, X. Yan, P. S. Yu, and T. Wu, “Pathsim: Meta path-
based top-k similarity search in heterogeneous information networks,”
Proceedings of the VLDB Endowment, vol. 4, no. 11, pp. 992–1003,
2011.
[70] V. N. Ioannidis, D. Berberidis, and G. B. Giannakis, “Graphsac: Detect-
ing anomalies in large-scale graphs,” arXiv preprint arXiv:1910.09589,
2019.
[71] B. A. Miller, M. C¸ amurcu, A. J. Gomez, K. Chan, and T. Eliassi-Rad,
“Improving robustness to attacks against vertex classification,” 2019.
[72] K. Zhou, T. P. Michalak, and Y. Vorobeychik, “Adversarial robustness of
similarity-based link prediction,” arXiv preprint arXiv:1909.01432, 2019.
[73] I. J. Goodfellow, J. Shlens, and C. Szegedy, “Explaining and harnessing
adversarial examples,” arXiv preprint arXiv:1412.6572, 2014.
[74] S. Rendle, C. Freudenthaler, Z. Gantner, and L. Schmidt-Thieme, “Bpr:
Bayesian personalized ranking from implicit feedback,” in Proceedings
of the twenty-fifth conference on uncertainty in artificial intelligence.
AUAI Press, 2009, pp. 452–461.
[75] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” in Advances in
neural information processing systems, 2017, pp. 5998–6008.
[76] S. Kullback and R. A. Leibler, “On information and sufficiency,” The
annals of mathematical statistics, vol. 22, no. 1, pp. 79–86, 1951.
16
[77] H. Von Stackelberg, Market structure and equilibrium. Springer Science
& Business Media, 2010.
[78] D. M. Powers, “Evaluation: from precision, recall and f-measure to roc,
informedness, markedness and correlation,” 2011.
[79] K. Boyd, K. H. Eng, and C. D. Page, “Area under the precision-recall
curve: point estimates and confidence intervals,” in Joint European
conference on machine learning and knowledge discovery in databases.
Springer, 2013, pp. 451–466.
[80] M. E. Newman, “Mixing patterns in networks,” Physical Review E,
vol. 67, no. 2, p. 026126, 2003.
[81] M. E. Newman and M. Girvan, “Finding and evaluating community
structure in networks,” Physical review E, vol. 69, no. 2, p. 026113,
2004.
[82] L. Danon, A. Diaz-Guilera, J. Duch, and A. Arenas, “Comparing com-
munity structure identification,” Journal of Statistical Mechanics: Theory
and Experiment, vol. 2005, no. 09, p. P09008, 2005.
[83] J. M. Santos and M. Embrechts, “On the use of the adjusted rand index
as a metric for evaluating supervised classification,” in International
conference on artificial neural networks. Springer, 2009, pp. 175–184.
[84] L. L¨ u and T. Zhou, “Link prediction in complex networks: A survey,”
Physica A: statistical mechanics and its applications, vol. 390, no. 6, pp.
1150–1170, 2011.
[85] A. K. McCallum, K. Nigam, J. Rennie, and K. Seymore, “Automating
the construction of internet portals with machine learning,” Information
Retrieval, vol. 3, no. 2, pp. 127–163, 2000.
[86] P. Sen, G. Namata, M. Bilgic, L. Getoor, B. Galligher, and T. Eliassi-Rad,
“Collective classification in network data,” AI magazine, vol. 29, no. 3,
pp. 93–93, 2008.
[87] A. Madry, A. Makelov, L. Schmidt, D. Tsipras, and A. Vladu, “Towards
deep learning models resistant to adversarial attacks,” arXiv preprint
arXiv:1706.06083, 2017.