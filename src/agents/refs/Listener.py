from ai_engine import UAgentResponse, UAgentResponseType
 

class GenerateNews(Model):
    news_type: str
 

generate_news_protocol = Protocol("Generate News")
 

@generate_news_protocol.on_message(model=GenerateNews, replies=UAgentResponse)
async def on_generate_news_request(ctx: Context, sender: str, msg: GenerateNews):
    ctx.logger.info('Generating News')
    ctx.logger.info(f'User have selected {msg.news_type} category')
    message = "This is some dummy news!"

    await ctx.send(sender, UAgentResponse(
            message= message,
            type=UAgentResponseType.FINAL
            )
    )


agent.include(generate_news_protocol)