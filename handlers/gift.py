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
            " Socks are cool, everyone loves socks! Here are some I suggest! --- https://www.amazon.com/Fruit-Loom-Heavy-Reinforced-Socks/dp/B005FYNXGO/ref=sr_1_3?keywords=male+socks&qid=1556570092&s=gateway&sr=8-3"
            " Video games are pretty popular and can be inexpensive, how about this one? --- https://www.amazon.com/Mortal-Kombat-11-PlayStation-4/dp/B07L6KD1K3/ref=sr_1_3?crid=DDX0LRC1MFJO&keywords=mortal+kombat+11&qid=1556570169&s=gateway&sprefix=mortal+%2Caps%2C148&sr=8-3",
            " Here are some Nikes that are pretty polular right now. --- https://www.amazon.com/Jordan-Rings-Royal-Black-White-Leather/dp/B06XYVP49L/ref=sr_1_299?keywords=mens+nike&qid=1556570277&s=gateway&sr=8-299",
            " Everyone loves a good laugh, I think this would be pretty funny. --- https://www.amazon.com/Worlds-Farter-Father-T-Shirt-X-Large/dp/B00XU93ZK0/ref=sr_1_3?keywords=funny+gift+for+dad&qid=1556570309&s=gateway&sr=8-3"
        ]
        female_gift_ideas = [
            " Candles are always nice, How about this one. --- https://www.amazon.com/Yankee-Candle-Large-Home-Sweet/dp/B000WUFVR0/ref=sr_1_26?keywords=candle&qid=1556570330&s=gateway&sr=8-26",
            " Flowers can be well priced, Here is one. --- https://www.amazon.com/Jackcsale-Romantic-Wedding-Valentines-Confession/dp/B01JFPKNRA/ref=sr_1_41?keywords=bouquet&qid=1556570451&s=gateway&sr=8-41",
            " Jewelry can be up there is price, Here is an example. --- https://www.amazon.com/Princess-14K-Classic-Diamond-Engagement/dp/B00JRGDME4/ref=sr_1_3?keywords=diamond+ring&qid=1556570535&s=gateway&sr=8-3",
            " Everyone loves a good laugh, I think this would be pretty funny. --- https://www.amazon.com/Mommin-Premium-Birthday-Friend-Present/dp/B01MUC28T3/ref=sr_1_11?keywords=funny+gift+for+mom&qid=1556570585&s=gateway&sr=8-11"
        ]
        sibling_gift_ideas = [
            " Keychains are cheap here are some I recommend. --- https://www.amazon.com/Disney-Princess-Keychain-Dangler-Figurine/dp/B01M758A0O/ref=sr_1_1?keywords=keychain+moana&qid=1556570767&s=gateway&sr=8-1",
            " Siblings are always wanting food, and a free meal can be nice.",
            " Everyone loves having fun, You can use this to have fun with your siblings. --- https://www.amazon.com/Nintendo-Switch-Neon-Red-Blue-Joy/dp/B01MUAGZ49/ref=sr_1_3?keywords=Nintendo+switch&qid=1556570893&s=gateway&sr=8-3",
            " T-shirts can be funny, How about this? --- https://www.amazon.com/Have-A-Garbage-Day-T-shirt/dp/B07H98JLRD/ref=sr_1_9?keywords=garbage+t-shirt&qid=1556570930&s=gateway&sr=8-9"
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
            
