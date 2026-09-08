def create_handoff(
    sender,
    receiver,
    task_id,
    result,
    next_instruction
):

    from message import Message

    return Message(
        sender=sender,
        receiver=receiver,
        message_type="TASK_HANDOFF",
        task_id=task_id,
        payload={
            "previous_result":
                result,

            "next_instruction":
                next_instruction
        }
    )