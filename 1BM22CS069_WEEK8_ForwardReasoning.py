class ForwardChaining:
    def __init__(self, kb, query):
        """
        Initialize with knowledge base (kb) and query.
        kb: list of definite clauses in the form of tuples (premises, conclusion)
        query: the fact to prove
        """
        self.kb = kb  # Knowledge Base: list of rules [(premises, conclusion), ...]
        self.query = query  # Query to prove
        self.facts = set()  # Initially empty set of known facts
        self.new_facts = set()  # Newly inferred facts

    def standardize_variables(self, rule):
        """
        Standardizes variables in a rule by renaming them to avoid conflicts.
        Returns the standardized rule.
        """
        premises, conclusion = rule
        return premises, conclusion  # Simplified: No renaming in this implementation

    def is_fact_derived(self, fact):
        """
        Checks if a fact is already derived (exists in known facts).
        """
        return fact in self.facts

    def can_infer(self, premises):
        """
        Checks if all premises of a rule are satisfied by the current facts.
        """
        return all(premise in self.facts for premise in premises)

    def infer_new_fact(self, conclusion):
        """
        Adds a new fact to the knowledge base if it hasn't been added already.
        """
        if conclusion not in self.facts and conclusion not in self.new_facts:
            self.new_facts.add(conclusion)

    def forward_chain(self):
        """
        Perform forward chaining to derive new facts and check if the query is provable.
        Returns True if the query can be proved, False otherwise.
        """
        # Initialize known facts in the KB (rules without premises)
        for premises, conclusion in self.kb:
            if not premises:  # A rule with no premises is a fact
                self.facts.add(conclusion)

        while True:
            self.new_facts = set()  # Reset newly inferred facts in each iteration

            for rule in self.kb:
                premises, conclusion = self.standardize_variables(rule)
                if self.can_infer(premises):
                    self.infer_new_fact(conclusion)

            # Add all newly inferred facts to the set of known facts
            self.facts.update(self.new_facts)

            # Check if the query is among the known facts
            if self.query in self.facts:
                return True  # Query proved

            # If no new facts are derived, stop the loop
            if not self.new_facts:
                break

        return False  # Query cannot be proved


if __name__ == "__main__":
    # Get user input for the knowledge base
    print("Enter the number of rules in the Knowledge Base:")
    num_rules = int(input())

    kb = []
    print("Enter each rule in the format 'premise1,premise2,... => conclusion' (leave premises empty for facts):")
    for _ in range(num_rules):
        rule = input().strip()
        if "=>" in rule:
            premises, conclusion = rule.split("=>")
            premises = [p.strip() for p in premises.split(",") if p.strip()]
            conclusion = conclusion.strip()
            kb.append((premises, conclusion))
        else:
            kb.append(([], rule.strip()))  # Fact with no premises

    # Get the query
    print("Enter the query to be proved:")
    query = input().strip()

    # Perform Forward Chaining
    fc = ForwardChaining(kb, query)
    result = fc.forward_chain()

    # Output the result
    if result:
        print(f"The query '{query}' is PROVABLE.")
    else:
        print(f"The query '{query}' CANNOT be proved.")

