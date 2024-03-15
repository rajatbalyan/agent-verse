from ai_engine import UAgentResponse, UAgentResponseType
from pydantic import Field

class Booking(Model):
    symptoms : str = Field("List of symptoms related to the sickess that you have: ")
    disease : str = Field("Disease that matches with the symptom provided")
    doctor: str = Field("Doctors found that matches the most with the given Symptoms and Disease")


checkup_protocol = Protocol("Medical Assist System")
@checkup_protocol.on_message(model=Booking, replies = UAgentResponse)
async def on_medical_analysis(ctx: Context, sender: str, msg: Booking):
    report_data = f"""
        Report for your medical analysis ----
        
        Symptoms: {msg.symptoms}
        Disease: {msg.disease}
        Doctor Assigned: {msg.doctor}
    """
    await ctx.send(sender, UAgentResponse(message = report_data, type = UAgentResponseType.FINAL))



agent.include(checkup_protocol)