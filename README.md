# Igor — Twitter Reply Experiment

A historical Python experiment combining **Twitter mentions, sentiment analysis, and intent classification** to generate replies. It uses Tweepy, TextBlob, NLTK, and a TensorFlow/tflearn model.

## How the source works

1. `main.py` creates a Twitter client and polls in a loop, waiting 30 seconds between iterations.
2. The client reads mentions and cleans their leading account mention.
3. `TextAnalyzer` uses TextBlob translation and sentiment, then a bag-of-words model to select a response.
4. The client publishes replies and remembers processed IDs in memory for that session.

The method named `retweet()` actually calls `update_status()` with the original post ID. It publishes a reply rather than performing a retweet operation.

## Source map

| File | Purpose |
| --- | --- |
| [main.py](main.py) | Polling entry point. |
| [TwitterClient.py](TwitterClient.py) | Authentication, mention retrieval, and publishing. |
| [TextAnalyzer.py](TextAnalyzer.py) | Polarity and response selection. |
| [training_model.py](training_model.py) | Vocabulary preparation, network construction, and checkpoint loading. |
| [intents.json](intents.json) | Intent patterns and candidate replies. |
| [feelings.json](feelings.json) | Additional response phrases. |
| [settings.py](settings.py) | Credential settings read by the client. |

## Environment preparation

There is no dependency manifest or verified reproducible installation. The source imports Tweepy, TextBlob, NLTK, NumPy, TensorFlow, tflearn, and BeautifulSoup. It uses older APIs such as `tensorflow.reset_default_graph()` and TextBlob translation; installing current package versions is not a verified setup.

Review the client, model, and settings before preparing an isolated compatible environment. NLTK tokenization data and checkpoint compatibility also need to be resolved. Credentials are read from `CONSUMER_KEY`, `CONSUMER_SECRET`, `ACCESS_TOKEN`, and `ACCESS_TOKEN_SECRET` in `settings.py`; there is no `.env` loader.

## Execution and limitations

`python main.py`, run from the repository root, starts the live account workflow. It is not a dry run and can publish real replies. This documentation update did not connect an account or execute the loop.

Importing `training_model.py` performs file and model initialization. An undefined `deff` reference forces its cache-loading block into the fallback path, rewriting `data.pickle`. Model training is commented out, and checkpoint-load failures are swallowed. Other broad exception handlers can hide authentication and publishing errors. Reply deduplication is not persisted across restarts.

There is no automated test suite. Review these limitations before treating the bot as a working deployment; the repository is best approached as a source-study project.
