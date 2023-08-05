### Alexa UTPL Global Campus Bot

A chat bot made with Alexa, ChatGPT and Arduino. It uses an alexa skill for interacting with users. It answers different questions using an external database (an excel file). Also controls an IoT circuit using Arduino IoT cloud API REST.

### 📦 Installation

Clone the repository and install the dependencies:

```
pip install -r requirements.txt
```

### 💬 ChatGPT

ChatGPT utils can be found at `chatgpt.py`:

```python
import time
start = time.time()
response = ask_to_chatgpt_v2("what's the physics?", max_tokens=100)
end = time.time()
print(f"elapsed time: {end - start} secs.")
```

### 💾 Database

The database uses pandas to read and make queries to some csv/excel files.

```python
db = Database()

db.load("dbutplcampus.csv")

print("Ciudades: ", db.get_all_cities())
print("Paises: ", db.get_all_countries())
print("Continentes: ", db.get_all_continents())
print("Institutions: ", db.get_institutions(randomized=True))
print("careers: ", db.get_careers())
print("convenios: ", db.get_convenios())
print("objetivos: ", db.get_objetivos())
```
