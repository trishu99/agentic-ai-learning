def agent_loop(task):
    while True:
        thought = llm_think(task)
        if thought == "DONE":
            break
        action = choose_action(thought)
        result = execute(action)
        task = update_context(task, result)
