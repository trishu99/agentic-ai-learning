## LLM Fundamentals

- LLMs operate on tokens, not words
- Embeddings represent meaning as vectors
- Transformers use attention to focus on relevant context
- Pre-training gives general knowledge
- Fine-tuning shapes behavior
- Inference is prediction, not learning
- Temperature controls randomness (higher temp more randomness)
- System prompts define behavior
- Token limits affect cost and truncation


Agents:
- Think via tokens
- Fail due to context overflow
- Behave based on system prompts
- Cost money per token
- Need structured outputs
 
Understanding this = agent control

### Tokens
LLMs do NOT understand words.
They understand tokens.

A token is:
    a word
    OR part of a word
    OR punctuation
    OR whitespace

Tokenization is model-specific

    Prompt tokens + Response tokens ≤ Context window

### Embeddings

Embeddings are:
    Numbers that represent meaning

Each word/sentence → vector
Similar meaning → closer vectors

LLMs don’t “read”
➡️ They calculate distances in vector space

### Transformer = Attention + Layers

Transformers answer one question repeatedly:
    “What should I pay attention to right now?”

Attention (The Brain of LLMs)
Layers (Depth of Thinking)

LLMs do not reason like humans
They simulate reasoning via probability + attention

### Pre-training vs Fine-tuning
Pre-training - Trained on massive internet text - general brain
Fine-tuning - Smaller curated dataset - sharp, specific brain

Most agent behavior comes from prompting, not fine-tuning.

Fine-tuning = expensive
Prompting = flexible

### Training vs Inference
Training - Learning
Inference - Asking questions

### Temperature

More temp -> more randomness

### System vs User Prompt

System prompt -> Sets personality & behavior, Strongest influence
User prompt -> Task input

Agents rely heavily on system prompts.

### Token Limits
Response is truncated
Prompt tokens remain unchanged

