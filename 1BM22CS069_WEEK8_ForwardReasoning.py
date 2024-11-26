class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        """Add a fact to the knowledge base."""
        self.facts.add(fact)

    def add_rule(self, premise, conclusion):
        """Add a rule with premises and conclusions to the knowledge base."""
        self.rules.append((premise, conclusion))

    def forward_chain(self, query):
        """Performs forward chaining to infer facts and check if the query is provable."""
        # Keep track of facts that can be inferred
        inferred = set(self.facts)
        new_facts = set(self.facts)
        all_inferred_facts = list(self.facts)  # To keep track of all facts inferred
        
        # Loop until no new facts can be derived
        while new_facts:
            temp_facts = set()
            for premise, conclusion in self.rules:
                # If all premises of a rule are in the inferred facts, infer the conclusion
                if all(p in inferred for p in premise):
                    if conclusion not in inferred:
                        temp_facts.add(conclusion)
            # Add the new facts to the inferred facts
            new_facts = temp_facts
            inferred.update(new_facts)
            all_inferred_facts.extend(new_facts)  # Add new facts to the list

            # If the query is found in the inferred facts, return True
            if query in inferred:
                return True, all_inferred_facts  # Query is provable, return the inferred facts
        return False, all_inferred_facts  # Query cannot be derived

def get_input():
    """Function to get user input for facts, rules, and queries."""
    kb = KnowledgeBase()
    
    print("Enter facts (enter 'done' when finished):")
    while True:
        fact = input("Fact (e.g., A(John)): ")
        if fact.lower() == 'done':
            break
        kb.add_fact(fact)
    
    print("Enter rules (enter 'done' when finished):")
    while True:
        rule_input = input("Rule (e.g., A(x),B(x) => C(x)): ")
        if rule_input.lower() == 'done':
            break
        # Extract premise and conclusion from user input
        premise_conclusion = rule_input.split('=>')
        if len(premise_conclusion) == 2:
            premise = premise_conclusion[0].strip().split(',')
            conclusion = premise_conclusion[1].strip()
            kb.add_rule(premise, conclusion)
    
    query = input("Enter the query you want to prove (e.g., C(John)): ")
    return kb, query

def main():
    # Get input from the user
    kb, query = get_input()
    
    # Perform forward chaining to prove the query
    result, inferred_facts = kb.forward_chain(query)
    
    # Display results
    if result:
        print(f"The query '{query}' can be proven!")
    else:
        print(f"The query '{query}' cannot be proven.")
    
    print("\nAll inferred facts:")
    for fact in inferred_facts:
        print(fact)

if __name__ == "__main__":
    main()
