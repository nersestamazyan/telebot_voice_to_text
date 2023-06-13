WORKDIR = "tmp_directory/"
TELEGRAM_DOWNLOAD_URL = 'https://api.telegram.org/file/bot'
HELP_COMMAND_RESPONSE = """This bot can handle the following commands:
/start - Start the bot and receive a welcome message.
/help - Get information about the bot and available commands."""
START_COMMAND_RESPONSE = "Hello! Welcome to Audio to Text Bot. You can send me a voice message and I'll return the text"

REF_TO_VOICE_1 = "It was the best of times. It was the worst of times. It was the age of wisdom. It was the age " \
                 "of foolishness. It was the epoch of belief. It was the epoch of incredulity. It was the " \
                 "season of the light. It was the season of darkness. It was the spring of hope. It was the " \
                 "winter of despair. We had everything before us. We had nothing before us. We were all going " \
                 "direct to heaven. We were all going direct the other way. In short, the period was so far " \
                 "like the present period that some of its noisiest authorities insisted on its being received " \
                 "for good. Or for evil in the superlative degree of comparison only."

REF_TO_VOICE_2 = "His palms are sweaty, knees weak, arms are heavy There's vomit on his sweater already, mom's spaghetti He's " \
                 "nervous, but on the surface he looks calm and ready to drop bombs But he keeps on forgetting what he wrote " \
                 "down, the whole crowd goes so loud He opens his mouth, but the words won't come out He's choking how, " \
                 "everybody's joking now The clock's run out, time's up, over, blaow! Snap back to reality Oh, there goes " \
                 "gravity Oh, there goes Rabbit, he choked He's so mad, but he won't give up that easy, no He won't have it, " \
                 "he knows his whole back's to these ropes It don't matter, he's dope He knows that but he's broke He's so " \
                 "stagnant, he knows when he goes back to his mobile home, that's when it's Back to the lab again, " \
                 "yo This whole rhapsody He better go capture this moment and hope it don't pass him"

REF_TO_VOICE_3 = "The story offered here takes place about a hundred years prior to the events described in A Game of " \
                  "Thrones. The spring rains had softened the ground, so Dunk had no trouble digging the grave. He " \
                  "chose a spot on the western slope of a low hill, for the old man had always loved to watch the " \
                  "sunset. Another day done, he would sigh. And who knows what the morrow will bring us, eh, " \
                  "Dunk?  Well, one morrow had brought rains that soaked them to the bones, and the one after had " \
                  "brought wet, gusty winds, and the next a chill. By the fourth day the old man was too weak to ride, " \
                  "and now he was gone. Only a few days past he had been singing as they rode, the old song about " \
                  "going to Gulltown to see a fair maid, but instead of Gulltown he'd sung of Ashford. Off to Ashford " \
                  "to see the fair maid, heigh-ho, heigh-ho, Dunk thought miserably as he dug."

REF_LIST = [
    REF_TO_VOICE_1,
    REF_TO_VOICE_2,
    REF_TO_VOICE_3
]

PATH_OF_TEST_WAV_FILES = "tests/"
