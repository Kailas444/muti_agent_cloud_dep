
class PlannerAgent:
    def plan(self, query):
        if "calculate" in query:
            return "use_calculator"
        return "use_rag"
