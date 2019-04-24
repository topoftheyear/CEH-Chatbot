import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler

class Module(HandlerModule):
    def __init__(self):
        super().__init__("gift", persist_state=False)


    def init_handlers(self):

        self.handlers.append( GiftHandler() )


class GiftHandler(MessageHandler):
    def __init__(self):
        self.signal = "!gift"

        # params to dispay in help meesages
        self.params = "a gift question"

        # displayed when !help is called
        self.short_description = " Gives a gift idea for a person"

        # displatyed when !help test is called
        self.long_description = " Gives a gift idea for the specified person"


    async def handle_message(self, client, message, state):
        # keywords to look for when deciding on a gift, who its going to | type of gift
        cheap_keywords = ["cheap", "inexpensive", "low cost", "doesn't cost much"]
        medium_price_keywords = ["nothing too expensive", "moderate price", "not too expensive"]
        expensive_keywords = ["expensive", "something nice", "fancy", "pricey", "nice"]
        funny_keywords = ["funny", "make them laugh", "joke"]
        dad_keywords = ["dad", "father"]
        mom_keywords = ["mom", "mother"]
        sibling_keywords = ["brother", "sister", "sibling"]

        # gift ideas are sorted by price and function of the gift.
        # positions 1-3 are gifts from a low price to a high price respectively.
        # position 4 is a funny gift idea.
        male_gift_ideas = [
            " Socks are cool, everyone loves socks! Here are some I suggest!"
            " Video games are pretty popular and can be inexpensive, how about this one?",
            " Here are some Nikes that are pretty polular right now.",
            " Everyone loves a good laugh, I think this would be pretty funny."
        ]
        female_gift_ideas = [
            " female low price",
            " female medium price",
            " female high price",
            " female funny gift"
        ]
        sibling_gift_ideas = [
            " sibling low price",
            " sibling medium price",
            " sibling high price",
            " sibling funny"
        ]

        # if the none of the criteria is met, this is the default gift idea
        gift_idea_for_you = "Hm, gift cards are always nice right?"


        if message.content.startswith(self.signal):
            if any(dad_word in message.content for dad_word in dad_keywords):
                if any(cheap_word in message.content for cheap_word in cheap_keywords):
                    gift_idea_for_you = male_gift_ideas[0]
                elif any(medium_word in message.content for medium_word in medium_price_keywords):
                    gift_idea_for_you = male_gift_ideas[1]
                elif any(expensive_word in message.content for expensive_word in expensive_keywords):
                    gift_idea_for_you = male_gift_ideas[2]
                elif any(funny_word in message.content for funny_word in funny_keywords):
                    gift_idea_for_you = male_gift_ideas[3]
                else:
                    gift_idea_for_you = "Something for your dad huh? How about this?"
            elif any(mom_word in message.content for mom_word in mom_keywords):
                if any(cheap_word in message.content for cheap_word in cheap_keywords):
                    gift_idea_for_you = female_gift_ideas[0]
                elif any(medium_word in message.content for medium_word in medium_price_keywords):
                    gift_idea_for_you = female_gift_ideas[1]
                elif any(expensive_word in message.content for expensive_word in expensive_keywords):
                    gift_idea_for_you = female_gift_ideas[2]
                elif any(funny_word in message.content for funny_word in funny_keywords):
                    gift_idea_for_you = female_gift_ideas[3]
                else:
                    gift_idea_for_you = "Something for your mom huh? How about this?"
            elif any(sibling_word in message.content for sibling_word in sibling_keywords):
                if any(cheap_word in message.content for cheap_word in cheap_keywords):
                    gift_idea_for_you = sibling_gift_ideas[0]
                elif any(medium_word in message.content for medium_word in medium_price_keywords):
                    gift_idea_for_you = sibling_gift_ideas[1]
                elif any(expensive_word in message.content for expensive_word in expensive_keywords):
                    gift_idea_for_you = sibling_gift_ideas[2]
                elif any(funny_word in message.content for funny_word in funny_keywords):
                    gift_idea_for_you = sibling_gift_ideas[3]
                else:
                    gift_idea_for_you = "Something for you sibling huh? How about this?"
            
            await message.channel.send(gift_idea_for_you) #client.send_message(message.channel, gift_idea_for_you)
            
