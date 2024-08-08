import java.util.ArrayList;
import java.util.List;

class InferenceEngine {
    // Define the rules of inference
    public boolean modusPonens(boolean p, boolean pImpQ) {
        return p && pImpQ;
    }

    public boolean modusTollens(boolean notQ, boolean pImpQ) {
        return notQ && pImpQ;
    }

    public boolean hypotheticalSyllogism(boolean pImpQ, boolean qImpR) {
        return pImpQ && qImpR;
    }

    public boolean disjunctiveSyllogism(boolean pOrQ, boolean notP) {
        return pOrQ && notP;
    }

    public boolean simplification(boolean pAndQ) {
        return pAndQ;
    }

    public boolean conjunction(boolean p, boolean q) {
        return p && q;
    }

    public boolean addition(boolean p) {
        return p;
    }

    public boolean resolution(boolean pOrQ, boolean notPOrR) {
        return pOrQ && notPOrR;
    }
    
    // Convert hypotheses from English to propositional logic
    public boolean[] convertHypotheses() {
        // Define propositions
        boolean p = true; // Ali works hard
        boolean q = true; // Ali is a dull boy
        boolean r = false; // Ali will not get the job
        
        boolean pImpQ = true; // If Ali works hard, then he is a dull boy
        boolean qImpR = true; // If Ali is a dull boy, then he will not get the job
        
        return new boolean[]{p, pImpQ, qImpR};
    }

    // Apply rules to prove the conclusion
    public boolean applyInferenceRules(boolean[] hypotheses) {
        boolean p = hypotheses[0];
        boolean pImpQ = hypotheses[1];
        boolean qImpR = hypotheses[2];

        boolean q = modusPonens(p, pImpQ); // Apply Modus Ponens
        boolean r = modusPonens(q, qImpR); // Apply Modus Ponens

        return r;
    }

    public static void main(String[] args) {
        InferenceEngine engine = new InferenceEngine();
        boolean[] hypotheses = engine.convertHypotheses();
        boolean result = engine.applyInferenceRules(hypotheses);

        System.out.println("Is the statement valid? " + result);
    }
}
