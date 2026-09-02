"""Small deterministic checks for generic pilot-learning regressions."""


def evaluate(scenario):
    data = scenario["input"]
    mechanism = scenario["mechanism"]

    if mechanism == "conversation_harvesting":
        complete = all(
            item.get("persisted_ref") and not item.get("chat_only", False)
            for item in data["material_items"]
        )
        return "harvest_complete" if complete else "material_state_only_in_chat"

    if mechanism == "context_fidelity":
        lossless = (
            set(data["source_refs"]) == set(data["compiled_refs"])
            and not data["materially_omitted"]
        )
        return "fidelity_preserved" if lossless else "semantic_drift"

    if mechanism == "elicitation_gate":
        if data["proposal_state"] == "candidate" and not data["authorized_decision"]:
            return "candidate_remains_candidate"
        return "promotion_authorized" if data["authorized_decision"] else "invalid_promotion"

    if mechanism == "generic_fit":
        if data["case_specific"] or data["generic_consumers"] < 2:
            return "remain_case_specific"
        return "sharpen_existing" if data.get("existing_mechanism") else "review_core_delta"

    if mechanism == "case_isolation":
        isolated = (
            not data["case_domain_terms_present"]
            and bool(data.get("case_return_ref"))
        )
        return "domain_neutral" if isolated else "case_leakage"

    if mechanism == "token_efficiency":
        lossless = (
            set(data["source_refs"]) == set(data["compiled_refs"])
            and not data["materially_omitted"]
        )
        efficient = data["compiled_tokens"] < data["baseline_tokens"]
        return "efficient_and_lossless" if efficient and lossless else "quality_or_efficiency_loss"

    raise ValueError(f"unknown mechanism: {mechanism}")
