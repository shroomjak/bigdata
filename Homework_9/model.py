import os
import keras
import numpy
import tensorflow_datasets

if not os.path.exists('imdb_lstm.keras'):
    BUFFER_SIZE = 10000
    BATCH_SIZE = 64
    VOCAB_SIZE = 1000
    EPOCHS = 10
    dataset, info = tensorflow_datasets.load(
        'imdb_reviews',
        with_info=True,
        as_supervised=True,
        data_dir='./imdb_reviews',
    )
    train_dataset, test_dataset = dataset['train'], dataset['test']
    train_dataset = train_dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
    test_dataset = test_dataset.batch(BATCH_SIZE)
    print('Gathering the vocabulary from the dataset...')

    encoder = keras.layers.TextVectorization(
        name='tv',
        max_tokens=VOCAB_SIZE
    )
    encoder.adapt(train_dataset.map(lambda text, label: text))
    print('...finished gathering the vocabulary from the dataset')

    model = keras.Sequential([
        encoder,
        # Use zero masking to handle the variable sequence lengths
        keras.layers.Embedding(input_dim=len(encoder.get_vocabulary()), output_dim=16, mask_zero=True),
        #keras.layers.Flatten(),
        #keras.layers.Dense(16, activation='relu'),
        keras.layers.LSTM(16),
        keras.layers.Dense(1, activation='sigmoid')  #Dense(10, activation='softmax')
        #keras.layers.Rescaling(scale=9, offset=1)
    ])
    model.compile(
        loss=keras.losses.BinaryCrossentropy(),  #keras.losses.SparseCategoricalCrossentropy(),
        optimizer=keras.optimizers.Adam(1e-3),
        metrics=['accuracy']
    )
    model.build(input_shape=(None,))   # For short summary
    model.summary()
    model.fit(
        train_dataset,
        epochs=EPOCHS,
        validation_data=test_dataset,
        validation_steps=3
    )
    model.export('imdb_lstm_export')
    numpy.save('imdb_lstm.voc.npy', encoder.get_vocabulary())

    sample_texts1 = numpy.array([
        'The movie was terrible. The animation and the graphics were a disaster. I would never recommend this movie.',
        'I liked the movie very much'
    ]).astype(object)
    predictions1 = model.predict(sample_texts1)
    for prediction, text in zip(predictions1, sample_texts1):
      print(prediction, '-', text)
else:
    model = keras.models.load_model('imdb_lstm.keras')
    #model.summary()  # -- works in python 2.10, keras 3.9.0, tensorflow 2.19.0; does not work in python 3.11, keras 3.6.0, tensorflow 2.18.0 after model loading
    model = keras.Sequential(
        [
            keras.layers.TextVectorization(vocabulary = numpy.load("imdb_lstm.voc.npy"))
            if l.name == 'tv'
            else l for l in model.layers
        ]
    )
    model.build(input_shape=(None,))
    model.summary()
sample_texts = numpy.array([
    'The movie was terrible. The animation and the graphics were a disaster. I would never recommend this movie.',
    'I liked the movie very much',
    'The movie was great. The animation and the graphics were perfect and very interesting and funny. I would recommend this movie to everyone.',
    '''One of Heather Welch’s jobs — before she was fired via an email giving her just 90 minutes to pack up and leave — was to prevent collisions between the ships and whales navigating the water along the US West Coast.
    Welch, who was an ecologist at the National Oceanic and Atmospheric Administration for nearly a decade, specialized in mapping the movement of marine animals. This information helped ships map their routes, and fisheries improve their catch, while avoiding accidentally scooping up and killing sea lions or turtles.
    Welch is just one of more than 1,000 people who in the past few weeks have been laid off from NOAA, the nation’s top weather and climate agency. It was already understaffed before President Donald Trump’s cuts, and there are more to come. The team Welch worked with, which provided crucial climate data to fisheries, was hit hard. Much of its work “will have to be scaled back, if not stopped entirely,” she told CNN.
    NOAA’s remit is wide, but one of its most critical roles is to observe the oceans. Multiple scientists told CNN the layoffs are taking expert eyes off the oceans at the worst possible time: as the oceans undergo extreme change — some of which remains largely unexplained — with deep impacts for humans, wildlife and economies.
    Global ocean temperatures shattered heat records for 450 straight days in 2023 and 2024, fueling more intense hurricanes, driving unexpectedly high sea level rise, killing marine life and causing catastrophic coral reef bleaching. A key system of ocean currents is showing signs of instability, and researchers are scrambling to understand if and when it could collapse, a potentially catastrophic event that would change weather in the Northern Hemisphere.
    Scuba divers above bleached coral at Looe Key Reef off the coast of Florida's Big Pine Key in July 2023. Record-breaking ocean heat has pushed corals to the brink over the past few years.
    
    It’s hard to overstate the role NOAA plays in ocean science.
    “If you’ve been to the ocean, or if you have experienced weather, you’ve been impacted by NOAA in some way,” said Tom Di Liberto, a climate scientist and former public affairs specialist at NOAA, who was also laid off in February.
    Data from the agency’s vast ocean monitoring networks, including ships, satellites and fleets of robotic buoys, feeds into near-term forecasts for weather and helps predict waves and tides. It gives a long-term picture, too, including projecting changes to reservoir water levels, snowpack and hurricane frequency.
    This information, provided publicly and for free, is leveraged by businesses. Fewer experts could reduce the quality of those much-used products.
    NOAA’s rich trove of data feeds climate models that allow scientists to look into the future and answer questions like “what is sea level rise going to look like in 50 years? What is weather going to look like in 50 years? How will agriculture change?” said Sarah Purkey, an assistant professor at the Scripps Institution of Oceanography.
    “Scattershot” firings have now “created holes all over NOAA” and the risks could be severe, Cooley said.
    Fishing nets are unloaded from NOAA's Bell M. Shimada fisheries survey vessel in Newport, Oregon, following a research expedition focused on understanding salmon and their ecosystems in 2022.
    
    Research tools, including an offshore sea life guide, are seen aboard the NOAA research vessel Fulmar near San Francisco.
    
    Scientists deploy an Argo float near Hawaii in 2018. The ocean robots dive miles deep into the ocean to track temperature, salinity and currents, then float back to the surface and connect to satellites to transmit the data.
    
    
    NOAA.
    A White House official told CNN “an extensive process was conducted to ensure that mission critical functions to fulfill the NOAA’s statutory responsibilities weren’t compromised.”
    NOAA’s science has implications for human lives. Hotter oceans fuel stronger storms and without accurate forecasts of their severity and where they will make landfall, “we’re going to have more people in harm’s way,” Cooley said.
    Climate change is also increasing the frequency of vibrio blooms, a flesh-eating bacteria found in seawater that infects people through cuts or by eating raw shellfish. Without the ability to identify conditions that could lead to a vibrio bloom, people in coastal regions and those who rely on shellfish “are in the crosshairs for an awful public health outcome,” Cooley said.
    “What we’re talking about here is a wholesale decrease in NOAA’s ability to support communities,” she added.
    Damage from Hurricane Helene in Horseshoe Beach, Florida, on September 28, 2024. Dozens of people were killed by the storm, which fed on exceptionally warm ocean water before making landfall and devastating western North Carolina with once-in-1,000-year flooding.
    
    Another big concern is how layoffs might affect NOAA’s work predicting and understanding El Niño and La Niña events, natural climate fluctuations which start in the Pacific Ocean and have huge impacts on global weather patterns.
    Agencies in other countries also monitor these patterns, including Peru and Japan, but the US plays a leading role. NOAA’s forecasts “can literally move global markets,” Di Liberto said.
    He worries the layoffs might affect international efforts to understand whether climate change affects the frequency and strength of El Niño and La Niña. The answer could mean “massive impacts in seasonal conditions across a huge portion of the globe,” he said.
    NOAA’s work also benefits industries.
    US fisheries are “among the best-managed in the world” because of NOAA, Cooley said. The agency provides information aimed at helping the industry maximize its harvest and keep fishing decades into the future without collapsing fish stocks.
    It’s too soon to understand the full impacts of the mass layoffs, but the first real test may come during a disaster like a hurricane. “When you stress a system during extremes, that’s when things can break,” Di Liberto said.
    NOAA's Bell M. Shimada fisheries survey vessel is unloaded after docking in Newport, Oregon, following a research expedition focused on understanding salmon in 2022. The agency provides information to help the fishing industry maximize its harvest without collapsing fish stocks.
    
    One thing scientists are sure about is there will be more climate change-driven disasters affecting the oceans and US coastlines over the next four years.
    A more long-term consequence is the number of early career scientists who were laid off. People like Allison Cluett, who was a research physical scientist at NOAA and part of a team studying changes in the Pacific Ocean to help fisheries make long-term decisions. It’s “heart breaking,” she told CNN, “the next generation of federal workers was just erased.”
    Firing young ocean scientists is a huge missed opportunity not least given the economic opportunities in the ocean economy, from food to clean energy, said Douglas McCauley, a professor of ocean science at the University of California Santa Barbara.
    Many could have been making vast amounts of money in the private sector but chose NOAA because they love the ocean, he told CNN. “By treating these scientist as if they are deadbeats … we will be lucky to ever successfully compete for the trillions in ocean wealth and be an ocean superpower,’ he said.
    Other countries may step into the gap. China is increasing its investment into ocean science, McCauley said. “Data is power, and that’s the same in the ocean as it is in any other domain,” he added, “with these cuts and this downsizing, we’re ceding that power.”''',


    ''' Interesting, until you get bored.
    With global tourism expanding at exponential rates and in innovative ways, what role can traditional institutions such as museums expect to play in contemporary travel itineraries? Can they still rely on the intrinsic value of their collections? Or do they need to start telling their stories with more force?
    Graveyards for stuff. Tombs for inanimate things.
    Their cavernous rooms and deep corridors reverberate with the soft, dead sounds of tourists shuffling and employees yawning.
    They’re like libraries, without the party atmosphere.
    Occasionally a shrill voice bounces down from a distant hallway: “No photos!” and I swivel to see something, anything, that might be interesting.
    But it’s not.
    Leering at a censured tourist for kicks says more about my own desperate situation than it does his, and anyway, it could have been me.
    I unwrap a biscuit to get through the next 50 yards of 19th-century teaspoons and the same shrill voice rings out again: “No food!”
    I’ve always hated museums.
    Yet twice or three times a year, I somehow find myself within one, shuffling from glass case to glass case, reading the little inscriptions, peering closely at the details, doing what any “good traveler” does.
    Two hours later I walk out bored, hungry and far less glad to be on vacation than when I went in.
    The main thing you learn in museums, it seems, is how not to run a museum.
    
    Amassing phantom university credits.
    
    “Vase: Iran; circa 15th century,” I’m told, time after time, as if this is all I need to know.
    As if what isn’t said I should know already.
    As if I’m not going to forget every dusty nugget of non-information the moment I walk away.
    “The Age of Algae: September 1-December 15; $15 only,” they offer, as if charging me for something I don’t care about is a privilege.
    Worst of all, there’s a climate of snobbery surrounding this whole industry.
    Confess that rather than stare glumly at an old beer chalice on a plinth you’d prefer to drink happily from a shiny new one in a pub, and you risk being outed as an ignoramus.
    Well, I’m outing myself. I’m a museo-phobe.
    It’s not that the hollow sound of shoes echoing off marble floors sends me into a fit of rage. It sends me into a shrug of ennui.
    Clearly the institutions behind museums are valuable. A lot of work is done outside the musty confines of their collections, from discovering new mammals in the jungles of Ecuador to creating and growing a huge global seed bank.
    They provide an umbilical link between our planet and our history to the future.
    But inside these crypts of curatorship, the connection to humankind falls short.
    If this is all you see of Doha's Museum of Islamic Art, count yourself lucky.
    
    Last year I visited Doha’s Museum of Islamic Art – a landmark at least as celebrated, if not more so, for its architecture than its contents, and no wonder.
    After the 200th glass case containing an old bowl – or was it a plate, or perhaps it was some more cutlery, who knows, who cares – I decided the photo opportunity across the sea was the best thing about the place.
    I’ve been to a sex museum in Amsterdam and never felt less titillated.
    I’ve been to a beer museum in Prague and never felt less intoxicated.
    
    Where’s the “muse” in all these museums? Where’s the theater?
    
    Millions of dollars, to see a rock.
    
    
    I put equivalent questions to several of the big museum names around the world, including the Smithsonian Institution, The British Museums Association and the Western Australian Museum.
    Most didn’t get back to me, but Ford W. Bell, president of the American Alliance of Museums, did. You can read his full, unedited letter here.
    As is usual when you ask any museum pro what the problem is, it comes down to money.
    “Since the Great Recession, our studies show that fully two-thirds of museums have reported financial stress,” says Bell.
    “Many have been forced to cut staff, hours and programs. At the height of the downturn, even the Metropolitan Museum of Art and the Getty – arguably the two richest museums in the country – cut their staffs.”
    Many of the world’s biggest and best museums are dependent on public money.
    London’s Natural History Museum needed £82 million ($128 million) to operate over 2012/2013, and nearly £46 million of this, 56%, came from government grants.
    The Smithsonian has been government funded to the tune of $811.5 million for 2013 – 65% of its total costs.
    Yet these are still cited as among their country’s best “free” activities.
    
    Is this really the best way to appreciate a Stradivarius?
    
    Insiders claim they generate far more money than they suck up. “One statistic I never tire of citing – for every $1 a municipality invests in cultural organizations, including museums, $7 are returned to the public coffers. That’s a return that would make Warren Buffett swoon,” says Bell.
    Fair enough, I don’t question the wider benefits of museums, economic or otherwise.
    But the collect-and-cage policy that defines the visible exhibits, much of which is not even visible most of the time, is anathema to an engaging experience.
    The exhibit just opened by the Smithsonian is a good example.
    “Souvenir Nation” showcases souvenirs from history and among its most noteworthy items are a brick from President Washington’s childhood home, a piece of Plymouth Rock chiseled off by a 19th-century tourist, locks of hair from former U.S presidents and a napkin belonging to Napoleon.
    So this icon of world museums is now proudly displaying an old brick, an old piece of rock, some hair and a napkin.
    
    Is there any other industry that could get away with this?
    
    This smacks of the most smugly provocative modern art, which insists that anything the curate deigns to put inside the building inevitably becomes “interesting.”
    Well, sorry. If you want me to fork out for some audio guide headphones, a gift shop key ring and even the $25 book at the end of it all, you need to do better.
    Where’s the relevance? Why, in places designed to celebrate life and all its variety, is there such a lack of vitality?
    Great for kids, but what about the rest of us?
    My trip two years ago to Hong Kong’s Science Museum convinced me that if there were a World Championship for Most Dreary Things To Do On Vacation, museums would be disqualified for going over the top.
    One of its centerpieces is a large ball bearing that trundles through a kind of miniature roller coaster on the hour. Between that and the Smithsonian’s brick, there lies a large pile of steaming desperation.
    Of course some artifacts speak for themselves.
    The Royal Armories in Leeds, England, shows off an 18th-century tunic on which you can still see the blood of the soldier who was speared, and presumably killed, while wearing it.
    A brief description suffices – imagination does the rest.
    But for the most part, museums need to stop relying on the supposed intrinsic value of their collections. Stop “presenting” when you should be flaunting. Give me a story. Show, don’t tell.
    
    Kids love museums, because they get to have fun. What about the rest of us?
    
    
    One area in which museums have struck some form of success seems to be with children.
    “Museums annually invest more than $2 billion in education programs each year,” says Bell, adding that U.S. museums welcome 90 million schoolchildren each year.
    Kids do seem to have a good time when pushing buttons, pulling levers and magnetizing soap bubbles (right up until they stop having a great time and turn into wailing bundles of hair and tears only a little more bored than the parents).
    But where’s the equivalent for adults? Why should over-16-year-olds, who still make up the significant majority of museum-goers, be subjected to stiff, dry, academia-laced presentations as if fun were a dirty word?
    
    Where’s your joy gone, museums?
    
    I can’t claim to have the answers, but I do know I expect a sense of traveling back in time when I visit a museum, of feeling like I was there while these things lived or were used, of feeling the ghosts of the past grab me by the hand and walk me around.
    Instead I get a sense of a classroom made of cold granite, the only sense of life emerging from the tourists.
    On the odd occasion a museum does succeed in transporting me into history, I’m ripped right back out at the end of the route by the gift shop-coffee shop-toilet triple-whammy.
    Nothing subverts a museum’s mission like a shiny, digitally printed banner broadcasting $4.95 replica Davids. ''',





      '''I found my ubuntu drivers for my laptop but I can't install them.
    They are some *.h files.
    How should I install them?
    Thanks :)
    Read the fucking manual.
    Manual? Fuck The Reading.
    I can't understand what you say.'''
]).astype(object)
# https://edition.cnn.com/2025/03/17/climate/noaa-layoffs-ocean-monitoring/index.html
# https://edition.cnn.com/travel/article/opinion-why-i-hate-museums/index.html

predictions = model.predict(sample_texts)
for prediction, text in zip(predictions, sample_texts):
    print('\n\n\n"Movie" rating', prediction*9 + 1, '/ 10 for the text:\n', text)
