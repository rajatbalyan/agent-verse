from ai_engine import UAgentResponse, UAgentResponseType

class News(Model):
    news : str

news_protocol = Protocol("News System")


@news_protocol.on_message(model=News, replies = UAgentResponse)
async def on_news_request(ctx: Context, sender: str, msg: News):
    final_news = f"News Received from Agent: {msg.news}"
    ctx.logger.info(f"Received news request from {sender} with prompt: {final_news}")
    await ctx.send(sender, UAgentResponse(message = final_news, type = UAgentResponseType.FINAL))


agent.include(news_protocol)