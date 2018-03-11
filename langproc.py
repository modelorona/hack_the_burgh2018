import requests
import random
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six
import sys

client = language.LanguageServiceClient()


# key = '789715b8c9ea48e6bafc27db256328fa'
# sentiment = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
# phrases = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases'
# language = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/languages'
# en = 'en'
# t = "application/json"
# headers = {
#     "Ocp-Apim-Subscription-Key": key,
#     "Content-Type": t,
#     "Accept": t
# }


# does hella work. text will have to be processed beforehand to take
def analyze(text):
    return_data = {}
    file = open('analyzed.txt', 'a')
    # text = u"{}".format(text)
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT
    )
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16
    result = client.analyze_entity_sentiment(document=document, encoding_type=encoding)

    file.write("Sentiment: {}, {}\n".format(sentiment.score, sentiment.magnitude))
    return_data["sentiment"] = sentiment
    # print()
    entities = []
    for entity in result.entities:
        new_entity = {}
        entity_mentions = []
        file.write("Mentions: \n")
        file.write(u'Name: {}\n'.format(entity.name))
        new_entity["name"] = entity.name
        new_entity["mentions"] = entity.mentions
        for mention in entity.mentions:
            file.write(u'  Begin Offset: {}\n'.format(mention.text.begin_offset))
            file.write(u'  Content: {}\n'.format(mention.text.content))
            file.write(u'  Magnitude: {}\n'.format(mention.sentiment.magnitude))
            file.write(u'  Sentiment: {}\n'.format(mention.sentiment.score))
            file.write(u'  Type: {}\n'.format(mention.type))
            entity_mentions.append({
                "begin_offset": mention.text.begin_offset,
                "content": mention.text.content,
                "magnitude": mention.sentiment.magnitude,
                "sentiment": mention.sentiment.score,
                "type": mention.type
            })
        new_entity["mentions"] = entity_mentions
        file.write(u'Salience: {}\n'.format(entity.salience))
        file.write(u'Sentiment: {}\n\n'.format(entity.sentiment))
        new_entity["salience"] = entity.salience
        new_entity["sentiment"] = entity.sentiment
        entities.append(new_entity)
    file.close()
    return_data["entities"] = entities

    tokens = client.analyze_syntax(document).tokens
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
    tks = []
    for token in tokens:
        tks.append({
            token.part_of_speech.tag: token.text.content
        })
        # print(u'{}: {}'.format(pos_tag[token.part_of_speech.tag],
        #                        token.text.content))
    return_data["tokens"] = tks
    print(return_data)
    return return_data
    # truncate it as azure has limit of 5000 characters
    # if len(text) > 5000:
    #     text = text[:5000]
    # response = requests.post(language, headers=headers, data={
    #     "documents": [
    #         {
    #             "id": str(random.randint(1, 100)),
    #             "text": text
    #         }
    #     ]
    # })
    # print(response.content)


analyze(
    u'Slovakia has quickly turned from what seemed to be a stable European Union country into chaos, in the wake of the unprecedented slayings of an investigative journalist and his fiancée. In a speech last month, President Andrej Kiska talked about his country as "successful, proud and self-confident." On March 4, however, he said Slovakia faces a "serious political crisis" triggered by the shooting deaths of Jan Kuciak and Martina Kusnirova. Police said the killing of Kuciak, a journalist, was likely linked to his work. Amid heated exchanges between the ruling coalition and the opposition, conspiracy theories spread by Prime Minister Robert Fico and his repeated verbal attacks on Kiska, a growing number of people have started to turn against the Fico government, threatening its existence. Tens of thousands of Slovaks rallied in massive anti-government protests across the country on Friday to demand a thorough investigation of the slayings, reflective of the political storm that has been intensifying daily since the bodies were found Feb. 25.The protesters packed a central square in Bratislava and other rallies were taking place in dozens of other places in Slovakia as well as abroad, the biggest since the 1989 Velvet Revolution. The organizers want foreign experts to join the team investigating the killings and the creation of "a new trustworthy government with no people who are suspected of corruption" or ties to organized crime. In his last unfinished story, Kuciak, 27, reported on the influence of the Italian Mafia in Slovakia and its possible ties to people close to Fico.That was followed by news that Slovak authorities had been informed by their Italian counterparts about a powerful Italian crime syndicate operating in Slovakia. Seven members of the group are suspects in the killings. They were detained last week and later released. "Slovakia is shaken as it has not been for a long time," protest organizer Karolina Farska said. The peaceful protesters had a message for Fico: "Resign," they repeatedly chanted. Conspiracy-minded PM When tens of thousands marched across the country and in cities around the world last week to honour Kuciak, many called on government ministers to resign. "Many have realized that the situation is becoming critical," said Michal Vasecka, an analyst from the Bratislava Policy Institute think-tank . "A fight started to prevent Slovakia from becoming another Hungary, an autocracy controlled by a small group of oligarchs." Reflecting the popular mood and growing protests, Kiska called for substantial changes in the government or for an early election to resolve the crisis. \"There\'s a huge public distrust of the state,\" Kiska said. "And many don\'t trust law enforcement authorities .... This distrust is justified. We crossed the line, things went too far and there\'s no way back."Fico fired back, accusing the president of destabilizing the country with help from Hungarian-American billionaire George Soros, with whom Kiska privately met in New York in September. Soros dismissed Fico\'s suggestion he might have anything to do with the president\'s proposals and the anti-government protests. \"Mr. Soros played no role in president Kiska\'s recent speech nor in recent demonstrations in Slovakia," his spokesperson Michael Vachon said earlier this week. Vasecka, the analyst, said Fico\'s conspiracy claims likely anger some people and contribute to their decision to join the protests because they hark back to the 1990s and the rule of authoritative Prime Minister Vladimir Meciar who led the country into international isolation. Meciar also targeted Soros. \"It reminds people of Meciar and also of communist rule. And a large part of society is very sensitive about it," Vasecka said. U.S. Ambassador Adam Sterling said in a statement that "as Slovak society wrestles with the implications of this crime, we urge all parties to refrain from resorting to the use of conspiracy theories and disinformation.\" A junior party in the ruling coalition has called for the resignation of Interior Minister Robert Kalinak as a condition to remain in the government. Thousands already demanded Kalinak\'s resignation last year after he was linked to earlier corruption scandals. The leadership of the coalition party known as Most-Hid will meet on Tuesday to decide on their role in the coalition. Meanwhile, the opposition has requested a parliamentary no-confidence vote on the government, but a date has yet to be set. Fico called the opposition request an \"attempted coup.\"')
