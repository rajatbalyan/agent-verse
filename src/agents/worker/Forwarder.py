from ai_engine import UAgentResponse, UAgentResponseType
from pydantic import Field


diseases = {
    "flu": "Flu Doctor",
    "bone": "Bone Doctor"
}

class UserInput(Model):
    symptoms : str = Field("List of symptoms related to the sickess that you have: ")

forward_protocol = Protocol("Medical Worker")


@forward_protocol.on_message(model=UserInput, replies = UAgentResponse)
async def on_symptoms_received(ctx: Context, sender: str, msg: UserInput):
    report = f"""
        For the given Symptoms: {msg.symptoms}, the doctor assigned is: {diseases[msg.symptoms]} 
        and disease is: {msg.symptoms}
    """
    await ctx.send(
        sender, 
        UAgentResponse(message = report, type = UAgentResponseType.FINAL)
    )

agent.include(forward_protocol)
