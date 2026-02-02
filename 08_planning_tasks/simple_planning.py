class TaskPlannerAgent:
    def __init__(self, goal: str):
        self.goal = goal
        self.plan = []

    def create_plan(self):
        """
        Breaks big goal into smaller steps
        """
        if "trip" in self.goal.lower():
            self.plan = [
                "Decide budget",
                "Select cities",
                "Plan daily itinerary",
                "Estimate cost",
                "Validate against budget"
            ]

    def execute_plan(self):
        print(f"🎯 Goal: {self.goal}\n")
        for step in self.plan:
            print(f"▶️ Executing step: {step}")

    def reflect(self):
        print("\n🔁 Reflection:")
        print("Plan looks reasonable. Ready for execution.")

    def reflect2(self, estimated_cost):
        print("\n🔁 Reflection:")
        if estimated_cost > 80000:
            print("❌ Budget exceeded. Revising plan...")
            self.plan.remove("Select cities")
            self.plan.insert(1, "Select cheaper cities")
        else:
            print("✅ Budget fits. Plan accepted.")





if __name__ == "__main__":
    agent = TaskPlannerAgent("Plan a 5-day Vietnam trip within ₹80,000")
    agent.create_plan()
    agent.execute_plan()
    agent.reflect2(estimated_cost=95000)


'''
Add Self-Correction


Lets simulate failure + retry.
eg: Cost exceeds budget → revise plan.

Update reflect() method


def reflect(self, estimated_cost):
    print("\n🔁 Reflection:")
    if estimated_cost > 80000:
        print("❌ Budget exceeded. Revising plan...")
        self.plan.remove("Select cities")
        self.plan.insert(1, "Select cheaper cities")
    else:
        print("✅ Budget fits. Plan accepted.")


    
call -> agent.reflect(estimated_cost=95000)


'''