# Summary 

Agentic AI Basics

Agent = LLM + goal + memory + tools + loop
Chatbots respond, agents decide
Workflows are static, agents are dynamic
Reasoning loops enable autonomy
ReAct = Reason + Act
Planning & reflection enable long tasks
Tools give agents real-world power

## What is an AI Agent?
Understand what makes something an agent (and why chatbots aren’t agents).

Agent = LLM + Goal + Memory + Tools + Control Loop

Chatbot = talks
Agent = acts

An agent:
- decides what to do next
- uses tools
- remembers past things
- works toward a goal

LLM	 --> Brain (reasoning, language)
Goal. --> 	What it’s trying to achieve
Memory --> 	Past context & knowledge
Tools. --> 	Ways to act in the world
Loop. --> 	Keeps thinking until goal is done

❌ Chatbot

Single request → single response
Stateless (mostly)
No tools
No autonomy

Example:

User: Summarize this article
Bot: Summary

✅ Agent

Multi-step reasoning
Uses tools
Remembers
Decides next action

Example:

Goal: Clean inbox
1. Read email
2. Decide spam or not
3. Call spam tool
4. Delete or archive
5. Repeat

Chatbots respond
Agents decide

## Workflow vs Agent

Workflow
Pre-defined steps
If/else logic
No autonomy

Agent
Chooses steps dynamically
Can retry
Can change plan

Agents handle:
uncertainty
partial information
evolving goals

## Autonomy, Planning & Reasoning Loops

🧠 Autonomy

Agent can:
decide when to act
decide what tool to call
decide when to stop

No human micromanagement.

Reasoning Loop (Core Agent Pattern)
Think → Act → Observe → Think → Act → ...

LLM:
reasons
chooses action
observes result
reasons again

Without loop → not an agent
One-shot tool calls ≠ agent.

## KEY AGENT PATTERNS

### ReAct Pattern (Reason + Act)

The agent explicitly:
- reasons in text
- chooses actions

Example

Thought: This email promises money → likely spam
Action: Call spam_classifier(email)
Observation: Confidence = 0.97
Final: Delete email

This is the foundation of most agents today.

Why ReAct works
- Prevents blind tool calls
- Makes reasoning visible
- Easy to debug

### Plan → Execute → Reflect

PLAN:
- Fetch data
- Analyze
- Take action

EXECUTE:
- Perform plan

REFLECT:
- Did it work?
- Retry or stop

Used by:
AutoGPT-style agents
Long-horizon tasks
Multi-tool workflows

### Tool-Calling Agents

Anything external:
API
Database
Python function
Search
Classifier

Agent Flow 
LLM decides →
Calls tool →
Gets result →
Decides next step

Tool call ≠ decision
LLM decides when & why

