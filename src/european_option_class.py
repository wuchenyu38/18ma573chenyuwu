{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "european_options_class.py",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/wuchenyu38/18ma573chenyuwu/blob/master/src/european_options_class.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "id": "ki7z0DDmXU9K",
        "colab_type": "code",
        "outputId": "f44f03d1-62e6-4383-894a-36cfcd67db75",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 351
        }
      },
      "cell_type": "code",
      "source": [
        "import european_options_class"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-e76a6d71c5a7>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0meuropean_options_class\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnumpy\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mscipy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstats\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mss\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'european_options_class'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ]
        }
      ]
    },
    {
      "metadata": {
        "id": "VaptkA_qXAYK",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "'''============\n",
        "Gbm class inherited from sde_1d\n",
        "============='''\n",
        "\n",
        "class Gbm:\n",
        "    def __init__(self,\n",
        "                 init_state = 100.,\n",
        "                 drift_ratio = .0475,\n",
        "                 vol_ratio = .2\n",
        "                ):\n",
        "        self.init_state = init_state\n",
        "        self.drift_ratio = drift_ratio\n",
        "        self.vol_ratio = vol_ratio"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "LRHBEEn9WIop",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        "'''=========\n",
        "option class init\n",
        "=========='''\n",
        "class VanillaOption:\n",
        "    def __init__(\n",
        "        self,\n",
        "        otype = 1, # 1: 'call'\n",
        "                  # -1: 'put'\n",
        "        strike = 110.,\n",
        "        maturity = 1.,\n",
        "        market_price = 10.):\n",
        "      self.otype = otype\n",
        "      self.strike = strike\n",
        "      self.maturity = maturity\n",
        "      self.market_price = market_price #this will be used for calibration\n",
        "      \n",
        "        \n",
        "    def payoff(self, s): #s: excercise price\n",
        "      otype = self.otype\n",
        "      k = self.strike\n",
        "      maturity = self.maturity\n",
        "      return np.max([0, (s - k)*otype])\n",
        "   "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "metadata": {
        "id": "xtPTlwEFW_jZ",
        "colab_type": "code",
        "colab": {}
      },
      "cell_type": "code",
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
