<!-- Source template: See: https://github.com/othneildrew/Best-README-Template/ -->
<a name="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">QA Over Database Application</h3>

  <p align="center">
    This project is a question-answering application that leverages local and open-source Large Language Models (LLMs). It utilizes your text database as its knowledge base or primary source of information.
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

With the rise of ChatGPT, which uses LLM (Large Language Model) as the backbone, it opens up many new opportunities for innovation. 

However, there are problems when we use commercial models like ChatGPT, particularly concerning privacy. When we use ChatGPT, it means we are willing to share our data for use by the platform. If it's not sensitive information, then it's okay. But what if it is?

Another problem is the source of information that ChatGPT uses to answer your questions. We don't know if the answer is based on a reliable or credible source or not.

So here open-source LLMs come in with the power to deploy your own LLMs on your local machine or server. Also, we can utilizing our database as the contextual source to enable the models to provide answers based on the content within the database, so we can make sure the answer really comes from the source we want.

I've created an application that employs an open-source Large Language Model (LLM). This LLM is stored on your local machine and utilizes your database as its knowledge base or primary source of information to perform question-answering tasks.


### Built With

Here is the tech stack and default ml models that I used:

* [Qdrant](https://github.com/qdrant/qdrant)
* [FastAPI](https://github.com/tiangolo/fastapi)
* [Langchain](https://github.com/langchain-ai/langchain)
* [Streamlit](https://github.com/streamlit/streamlit)
* [Docker](https://github.com/docker)
* [Llama 2 13b chat quantitized](https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ)
* [Multilingual e5 large](https://huggingface.co/intfloat/multilingual-e5-large)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

Here are the things you should fulfill first before installation.
* Download and install [python](https://www.python.org/downloads/).
* You need to install Docker first, follow the instruction [here](https://docs.docker.com/get-docker/) depends on your OS.
* Open your command-line interface and install/pull Qdrant image
  ```sh
  docker pull qdrant/qdrant
* Install docker-compose, only if you want running the app via docker later, follow the instruction [here](https://docs.docker.com/compose/install/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/rezkyws/local-qa-documents.git
   ```
2. Run Qdrant server
   ```sh
   docker run -p 6333:6333 -p 6334:6334 -v $(pwd)/qdrant_storage:/qdrant/storage qdrant/qdrant
   ```
3. Rename `.env.example` file to `.env`
4. Edit `.env` file and set up these environment variables
   * EMBEDDING_MODEL_DEVICE - Either `cpu` or `cuda`. Choose cuda if you want the embedding model to use GPU otherwise use cpu.
   * LLM_MODEL_DEVICE - Choose your cuda device. if you only have 1 gpu in your machine than set to `cuda:0`.
   * QDRANT_HOST - Your Qdrant server host. Default value is `localhost`.
   * QDRANT_PORT - Your Qdrant server port. Default value is `6333`.
   * QDRANT_COLLECTION_NAME - Your collection name in the Qdrant server that you want to use later as the source of information or knowledge base.
   * APP_PORT - The application port where this application running later.
5. Now, run the application with either this two methods
   * Run Natively (strongly suggest to use virtual environment such as conda venv to avoid conflicts) :
     * Install the dependencies first
       ```sh
       pip install -r requirements.txt
       ```
     * Run the application :
       ```sh
       python3 server.py build_ext --inplace
       ```
    * Run via container (docker)
      ```sh
      docker-compose up --build
      ```
6. Go to `gui` folder and run the gui/frontend with this command
   ```sh
   streamlit run Chat.py --server.port=3346
   ```
7. Done! if everything run successfully now open the apps on the browser and go to this link `localhost:3346` (default)
      
   ```
   const API_KEY = 'ENTER YOUR API';
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>
