# ConnectBot 
This bot helps you build a network with your ideal connections on LinkedIn. It automates the process of sending connection requests to users who match your specified criteria, saving you time and effort.

## 🚀 How to Run

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Datta-Lohith/ConnectBot.git
    cd ConnectBot
    ```

2. **Create Virtual Environment**:
  Run the following commands to create and run the project in a virtual environment.(In Windows)
    ```bash
    python -m venv virtual
    .\virtual\Scripts\activate 
    ```  
  Run the following commands to create and run the project in a virtual environment.(In Linux based OS)
    ```bash
    python -m venv virtual
    source \virtual\bin\activate
    ```

3. **Install Dependencies**:
  Ensure you have Python 3 installed. Then, install the required packages:
  - Ubuntu(Skip this step if Windows)
    ```bash
    sudo apt-get python3-tk python3-dev
    ```
  - Install from requirements.txt
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the Bot**:
  Open the `/setup` folder and enter your login details in [secrets.yaml](/setup/secrets.yaml). Adjust other settings in [config.yaml](/setup/config.yaml) as needed. Modify the note if needed at Line 114 in [connectBot.py](/connectBot.py). If you want to connect to people of specific companies, add the company names after the roles in the `config.yaml` file.


4. **Run the Bot**:
  Execute the following command to start the bot:
    ```bash
    python connectBot.py
    ```

## Note

If the error arises when activating the virtual environment on windows. Run the powershell as admin and run the following command.

```
set-executionpolicy remotesigned
```


## 📜 Disclaimer

**This program is for educational purposes only. By downloading, using, copying, replicating, or interacting with this program or its code, you acknowledge and agree to abide by all the Terms, Conditions, Policies, and Licenses mentioned, which are subject to modification without prior notice. The responsibility of staying informed of any changes or updates bears upon yourself. For the latest Terms & Conditions, Licenses, or Policies, please refer to [Connect Bot](https://github.com/Datta-Lohith/Connect-Bot). Additionally, kindly adhere to and comply with LinkedIn's terms of service and policies pertaining to web scraping. Usage is at your own risk. The creators and contributors of this program emphasize that they bear no responsibility or liability for any misuse, damages, or legal consequences resulting from its usage.**


## 🏛️ Terms and Conditions

Please consider the following:

- **LinkedIn Policies**: LinkedIn has specific policies regarding web scraping and data collection. The responsibility to review and comply with these policies before engaging, interacting, or undertaking any actions with this program bears upon yourself. Be aware of the limitations and restrictions imposed by LinkedIn to avoid any potential violation(s).

- **No Warranties or Guarantees**: This program is provided as-is, without any warranties or guarantees of any kind. The accuracy, reliability, and effectiveness of the program cannot be guaranteed. Use it at your own risk.

- **Disclaimer of Liability**: The creators and contributors of this program shall not be held responsible or liable for any damages or consequences arising from the direct or indirect use, interaction, or actions performed with this program. This includes but is not limited to any legal issues, loss of data, or other damages incurred.

- **Use at Your Own Risk**: It is important to exercise caution and ensure that your usage, interactions, and actions with this program comply with the applicable laws and regulations. Understand the potential risks and consequences associated with web scraping and data collection activities.

- **Chrome Driver**: This program utilizes the Chrome Driver for web scraping. Please review and comply with the terms and conditions specified for [Chrome Driver](https://chromedriver.chromium.org/home).


## ⚖️ License

Copyright (C) 2024 Datta Lohith Gannavarapu 

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

See [AGPLv3 LICENSE](LICENSE) for more info.


## 📞 Contact

For any inquiries, support, or feedback, please reach out via the following platforms:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/datta-lohith)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Datta-Lohith)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gdattalohith@gmail.com)

## ❤️ Support

If you find this project helpful and would like to support its development, consider giving it a star on GitHub or sharing it with your network. Your support is greatly appreciated!

![Project Views](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/Datta-Lohith/ConnectBot&title=People%20Used%20This%20Project)


[![GitHub Stars](https://img.shields.io/github/stars/Datta-Lohith/ConnectBot?style=social)](https://github.com/Datta-Lohith/ConnectBot/stargazers)