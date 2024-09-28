{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/RahmaIbrahimm/RahmaIbrahimm/blob/main/NER%20(1).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "uP3nnqV48RQX",
        "outputId": "540bd29d-40b3-43d4-e074-7af8319ff17e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.38.0-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Requirement already satisfied: transformers in /usr/local/lib/python3.10/dist-packages (4.44.2)\n",
            "Requirement already satisfied: torch in /usr/local/lib/python3.10/dist-packages (2.4.1+cu121)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.1.4)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (10.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.8.1)\n",
            "Collecting tenacity<9,>=8.1.0 (from streamlit)\n",
            "  Downloading tenacity-8.5.0-py3-none-any.whl.metadata (1.2 kB)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
            "  Downloading GitPython-3.1.43-py3-none-any.whl.metadata (13 kB)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog<5,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-4.0.2-py3-none-manylinux2014_x86_64.whl.metadata (38 kB)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from transformers) (3.16.1)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.23.2 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.24.7)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from transformers) (6.0.2)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.10/dist-packages (from transformers) (2024.9.11)\n",
            "Requirement already satisfied: safetensors>=0.4.1 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.4.5)\n",
            "Requirement already satisfied: tokenizers<0.20,>=0.19 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.19.1)\n",
            "Requirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.10/dist-packages (from transformers) (4.66.5)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from torch) (1.13.3)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch) (3.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from torch) (3.1.4)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from torch) (2024.6.1)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading gitdb-4.0.11-py3-none-any.whl.metadata (1.2 kB)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->torch) (2.1.5)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy->torch) (1.3.0)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
            "  Downloading smmap-5.0.1-py3-none-any.whl.metadata (4.3 kB)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
            "Downloading streamlit-1.38.0-py2.py3-none-any.whl (8.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.7/8.7 MB\u001b[0m \u001b[31m83.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading GitPython-3.1.43-py3-none-any.whl (207 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m207.3/207.3 kB\u001b[0m \u001b[31m16.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m91.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading tenacity-8.5.0-py3-none-any.whl (28 kB)\n",
            "Downloading watchdog-4.0.2-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.9/82.9 kB\u001b[0m \u001b[31m6.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m5.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
            "Installing collected packages: watchdog, tenacity, smmap, pydeck, gitdb, gitpython, streamlit\n",
            "  Attempting uninstall: tenacity\n",
            "    Found existing installation: tenacity 9.0.0\n",
            "    Uninstalling tenacity-9.0.0:\n",
            "      Successfully uninstalled tenacity-9.0.0\n",
            "Successfully installed gitdb-4.0.11 gitpython-3.1.43 pydeck-0.9.1 smmap-5.0.1 streamlit-1.38.0 tenacity-8.5.0 watchdog-4.0.2\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit transformers torch"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "Jh7PJTDA-IpY",
        "outputId": "554f1773-94fa-41c9-e4e5-bceb4d1948cc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.10/dist-packages (1.38.0)\n",
            "Requirement already satisfied: transformers in /usr/local/lib/python3.10/dist-packages (4.44.2)\n",
            "Requirement already satisfied: torch in /usr/local/lib/python3.10/dist-packages (2.4.1+cu121)\n",
            "Collecting pyngrok\n",
            "  Downloading pyngrok-7.2.0-py3-none-any.whl.metadata (7.4 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.1.4)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (10.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.8.1)\n",
            "Requirement already satisfied: tenacity<9,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.5.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Requirement already satisfied: watchdog<5,>=2.1.5 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.0.2)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from transformers) (3.16.1)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.23.2 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.24.7)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from transformers) (6.0.2)\n",
            "Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.10/dist-packages (from transformers) (2024.9.11)\n",
            "Requirement already satisfied: safetensors>=0.4.1 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.4.5)\n",
            "Requirement already satisfied: tokenizers<0.20,>=0.19 in /usr/local/lib/python3.10/dist-packages (from transformers) (0.19.1)\n",
            "Requirement already satisfied: tqdm>=4.27 in /usr/local/lib/python3.10/dist-packages (from transformers) (4.66.5)\n",
            "Requirement already satisfied: sympy in /usr/local/lib/python3.10/dist-packages (from torch) (1.13.3)\n",
            "Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch) (3.3)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from torch) (3.1.4)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from torch) (2024.6.1)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->torch) (2.1.5)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy->torch) (1.3.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
            "Downloading pyngrok-7.2.0-py3-none-any.whl (22 kB)\n",
            "Installing collected packages: pyngrok\n",
            "Successfully installed pyngrok-7.2.0\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit transformers torch pyngrok"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "Z7XS4_DCAY8W",
        "outputId": "cbd9bda6-b2a2-4e2d-ebc3-60da96d1dbfa"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "/bin/bash: -c: line 1: syntax error near unexpected token `newline'\n",
            "/bin/bash: -c: line 1: `ngrok authtoken <2mYPg4f33sGddKaAUCKnY87MK6n_7PbcMjZkdSoByWp2Q843L> # Replace <YOUR_AUTHTOKEN>'\n"
          ]
        }
      ],
      "source": [
        "!ngrok authtoken <2mYPg4f33sGddKaAUCKnY87MK6n_7PbcMjZkdSoByWp2Q843L> # Replace <YOUR_AUTHTOKEN>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "KK1RLnXLA48I",
        "outputId": "777d1d3c-07d6-4b54-b391-83e15468bbf8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: pyngrok in /usr/local/lib/python3.10/dist-packages (7.2.0)\n",
            "Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.10/dist-packages (from pyngrok) (6.0.2)\n"
          ]
        }
      ],
      "source": [
        "!pip install pyngrok"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true
        },
        "id": "bJEMck8r_ueD",
        "outputId": "449d0cc2-c4e7-4b22-f7c2-dc6491ef805d"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "WARNING:pyngrok.process.ngrok:t=2024-09-28T09:46:16+0000 lvl=warn msg=\"invalid tunnel configuration\" pg=/api/tunnels id=f24d30855e1d01ca err=\"yaml: unmarshal errors:\\n  line 1: field port not found in type config.HTTPv2Tunnel\"\n"
          ]
        },
        {
          "ename": "PyngrokNgrokHTTPError",
          "evalue": "ngrok client exception, API returned 400: {\"error_code\":102,\"status_code\":400,\"msg\":\"invalid tunnel configuration\",\"details\":{\"err\":\"yaml: unmarshal errors:\\n  line 1: field port not found in type config.HTTPv2Tunnel\"}}\n",
          "output_type": "error",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mHTTPError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pyngrok/ngrok.py\u001b[0m in \u001b[0;36mapi_request\u001b[0;34m(url, method, data, params, timeout, auth)\u001b[0m\n\u001b[1;32m    521\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 522\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0murlopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrequest\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mencoded_data\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    523\u001b[0m         \u001b[0mresponse_data\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdecode\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"utf-8\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36murlopen\u001b[0;34m(url, data, timeout, cafile, capath, cadefault, context)\u001b[0m\n\u001b[1;32m    215\u001b[0m         \u001b[0mopener\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_opener\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 216\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mopener\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdata\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    217\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36mopen\u001b[0;34m(self, fullurl, data, timeout)\u001b[0m\n\u001b[1;32m    524\u001b[0m             \u001b[0mmeth\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprocessor\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 525\u001b[0;31m             \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmeth\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    526\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36mhttp_response\u001b[0;34m(self, request, response)\u001b[0m\n\u001b[1;32m    633\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0;36m200\u001b[0m \u001b[0;34m<=\u001b[0m \u001b[0mcode\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;36m300\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 634\u001b[0;31m             response = self.parent.error(\n\u001b[0m\u001b[1;32m    635\u001b[0m                 'http', request, response, code, msg, hdrs)\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36merror\u001b[0;34m(self, proto, *args)\u001b[0m\n\u001b[1;32m    562\u001b[0m             \u001b[0margs\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mdict\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'default'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'http_error_default'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0morig_args\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 563\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_call_chain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    564\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36m_call_chain\u001b[0;34m(self, chain, kind, meth_name, *args)\u001b[0m\n\u001b[1;32m    495\u001b[0m             \u001b[0mfunc\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhandler\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmeth_name\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 496\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    497\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mresult\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.10/urllib/request.py\u001b[0m in \u001b[0;36mhttp_error_default\u001b[0;34m(self, req, fp, code, msg, hdrs)\u001b[0m\n\u001b[1;32m    642\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mhttp_error_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreq\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhdrs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 643\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mHTTPError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreq\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfull_url\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmsg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mhdrs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfp\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    644\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mHTTPError\u001b[0m: HTTP Error 400: Bad Request",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mPyngrokNgrokHTTPError\u001b[0m                     Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-15-dfa499a6594f>\u001b[0m in \u001b[0;36m<cell line: 10>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;31m# Start a new tunnel for Streamlit\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m \u001b[0mpublic_url\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mngrok\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconnect\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mport\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'8501'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m \u001b[0mpublic_url\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pyngrok/ngrok.py\u001b[0m in \u001b[0;36mconnect\u001b[0;34m(addr, proto, name, pyngrok_config, **options)\u001b[0m\n\u001b[1;32m    318\u001b[0m     \u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Creating tunnel with options: {options}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    319\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 320\u001b[0;31m     tunnel = NgrokTunnel(api_request(f\"{api_url}/api/tunnels\", method=\"POST\", data=options,\n\u001b[0m\u001b[1;32m    321\u001b[0m                                      timeout=pyngrok_config.request_timeout),\n\u001b[1;32m    322\u001b[0m                          pyngrok_config, api_url)\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/pyngrok/ngrok.py\u001b[0m in \u001b[0;36mapi_request\u001b[0;34m(url, method, data, params, timeout, auth)\u001b[0m\n\u001b[1;32m    541\u001b[0m         \u001b[0mlogger\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Response {status_code}: {response_data.strip()}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    542\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 543\u001b[0;31m         raise PyngrokNgrokHTTPError(f\"ngrok client exception, API returned {status_code}: {response_data}\",\n\u001b[0m\u001b[1;32m    544\u001b[0m                                     \u001b[0me\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0murl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    545\u001b[0m                                     status_code, e.reason, e.headers, response_data)\n",
            "\u001b[0;31mPyngrokNgrokHTTPError\u001b[0m: ngrok client exception, API returned 400: {\"error_code\":102,\"status_code\":400,\"msg\":\"invalid tunnel configuration\",\"details\":{\"err\":\"yaml: unmarshal errors:\\n  line 1: field port not found in type config.HTTPv2Tunnel\"}}\n"
          ]
        }
      ],
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "# Set your authtoken\n",
        "ngrok.set_auth_token(\"<YOUR_AUTHTOKEN>\") # Replace <YOUR_AUTHTOKEN>\n",
        "\n",
        "# Terminate any existing tunnels\n",
        "ngrok.kill()\n",
        "\n",
        "# Start a new tunnel for Streamlit\n",
        "public_url = ngrok.connect(port='8501')\n",
        "public_url"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}