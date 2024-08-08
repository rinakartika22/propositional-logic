class InferenceEngine:
    def modus_ponens(self, p, p_imp_q):
        """ Modus Ponens: If p and (p -> q) then q """
        return p and p_imp_q

    def modus_tollens(self, not_q, p_imp_q):
        """ Modus Tollens: If not q and (p -> q) then not p """
        return not_q and p_imp_q

    def hypothetical_syllogism(self, p_imp_q, q_imp_r):
        """ Hypothetical Syllogism: If (p -> q) and (q -> r) then (p -> r) """
        return p_imp_q and q_imp_r

    def disjunctive_syllogism(self, p_or_q, not_p):
        """ Disjunctive Syllogism: If (p or q) and not p then q """
        return p_or_q and not_p

    def simplification(self, p_and_q):
        """ Simplification: If (p and q) then p """
        return p_and_q

    def conjunction(self, p, q):
        """ Conjunction: If p and q then (p and q) """
        return p and q

    def addition(self, p):
        """ Addition: If p then (p or q) """
        return p

    def resolution(self, p_or_q, not_p_or_r):
        """ Resolution: If (p or q) and (not p or r) then (q or r) """
        return p_or_q and not_p_or_r

    def convert_hypotheses(self):
        """ Convert hypotheses from English to propositional logic """
        # Define propositions
        p = True  # Ali works hard
        q = True  # Ali is a dull boy
        r = False  # Ali will not get the job

        p_imp_q = True  # If Ali works hard, then he is a dull boy
        q_imp_r = True  # If Ali is a dull boy, then he will not get the job

        return p, p_imp_q, q_imp_r

    def apply_inference_rules(self, rule, hypotheses):
        p, p_imp_q, q_imp_r = hypotheses

        if rule == "modus_ponens":
            q = self.modus_ponens(p, p_imp_q)
            r = self.modus_ponens(q, q_imp_r)
        elif rule == "modus_tollens":
            not_r = not self.modus_tollens(r, q_imp_r)
            not_p = not self.modus_tollens(not_r, p_imp_q)
            r = not not_p
        elif rule == "hypothetical_syllogism":
            p_imp_r = self.hypothetical_syllogism(p_imp_q, q_imp_r)
            r = self.modus_ponens(p, p_imp_r)
        elif rule == "disjunctive_syllogism":
            p_or_q = p or q
            r = self.disjunctive_syllogism(p_or_q, not p)
        elif rule == "simplification":
            p_and_q = p and q
            r = self.simplification(p_and_q)
        elif rule == "conjunction":
            r = self.conjunction(p, q)
        elif rule == "addition":
            r = self.addition(p)
        elif rule == "resolution":
            p_or_q = p or q
            not_p_or_r = not p or r
            r = self.resolution(p_or_q, not_p_or_r)
        else:
            raise ValueError("Unknown rule of inference")

        return r

def main():
    engine = InferenceEngine()
    hypotheses = engine.convert_hypotheses()

    print("Select the rule of inference to use:")
    print("1. Modus Ponens")
    print("2. Modus Tollens")
    print("3. Hypothetical Syllogism")
    print("4. Disjunctive Syllogism")
    print("5. Simplification")
    print("6. Conjunction")
    print("7. Addition")
    print("8. Resolution")

    rule = input("Enter the number corresponding to the rule: ")

    rules = {
        "1": "modus_ponens",
        "2": "modus_tollens",
        "3": "hypothetical_syllogism",
        "4": "disjunctive_syllogism",
        "5": "simplification",
        "6": "conjunction",
        "7": "addition",
        "8": "resolution"
    }

    selected_rule = rules.get(rule)

    if selected_rule:
        result = engine.apply_inference_rules(selected_rule, hypotheses)
        print(f"Using {selected_rule}, the statement 'Ali will not get the job' is {result}")
    else:
        print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
