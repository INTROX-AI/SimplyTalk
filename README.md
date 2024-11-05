<p align="center">
  <a href="https://github.com/INTROX-AI"><img src="https://github.com/INTROX-AI/INTROX-AI/blob/efbf14c8c401c5db91b77b8aa85be947c966e798/assets/logo.gif" alt="SACHINBP1024" width="298" /></a> 
</p>
<p align="center">
  <a href="https://github.com/SACHINBP1024"><img src="https://github.com/user-attachments/assets/fea84d86-8f4a-4741-8afc-0961569d9300" alt="SACHINBP1024" width="298" /></a> 
</p>
<p align="center">
  <a href="https://github.com/SACHINBP1024/SimplyTalk"><img src="https://github.com/SACHINBP1024/SimplyTalk/blob/main/static/logo.png" alt="SimplyTalk" width="298" /></a> 
</p>

# SimplyTalk 📱🗣️

**SimplyTalk** is an innovative mobile application designed to transcribe external conversations and public announcements in real-time, particularly catering to the needs of deaf and hard-of-hearing individuals. 

## Project Synopsis 📋

SimplyTalk focuses on places where important public information is announced, such as railways, airports, and other public venues. Additionally, it offers a conversation mode for everyday social interactions. The app is tailored to minimize the text, simplifying complex speech into digestible, fast, and efficient readable content, ensuring a smoother user experience.

## Objective 🎯

- To provide a solution that bridges communication gaps for the deaf community.
- To make public announcements more accessible.
- To simplify and accelerate reading by processing information quickly and clearly.

## Modes of Operation 🚦

1. **Travel Mode**: Designed for places with public announcements like railways, airports, and bus terminals. This mode efficiently transcribes important audio announcements, highlighting the relevant information for easy reading.
2. **Conversation Mode**: This mode transcribes real-time conversations between individuals, simplifying them to enable quick and clear understanding.

## Key Features 🌟

- **Text Simplification**: A built-in lightweight language model will process and simplify text to be concise and easy to read.
- **Language Processing**: The app or device will support multilingual inputs, automatically detecting and transcribing speech in various languages.
- **Mini LLM Model Implementation**: By integrating a miniature large language model (LLM) within the wearable device, the app will be able to process and simplify text locally, without needing constant access to online resources.

## Multilingual Support 🌐

SimplyTalk will support multiple languages, making it versatile for different regions, ensuring inclusivity for all communities worldwide.

## Indian Sign Language (ISL) Integration 🤟

SimplyTalk will also support ISL, making it accessible for a wide range of people who are illiterate.

## Wearable Technology Integration ⌚

To enhance portability and convenience, SimplyTalk could evolve into a wearable device, like smart glasses or a wristband. This wearable version would transcribe conversations and announcements, further simplifying interaction by freeing up hands. The wearability would make the app more practical, especially in travel settings.

## Potential Benefits 🎁

- Accessibility for the deaf community, making public transportation and social interactions more inclusive.
- Easier and faster comprehension through simplified, minimal text.
- Multilingual transcription capabilities, ensuring use across diverse communities.
- Increased convenience via a wearable form factor for hands-free, on-the-go access.
- Integrated Indian Sign Language for easily accessible for illiterate people.

## Getting Started 🚀

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sachinbp1024/simplytalk.git
    cd simplytalk
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python main.py
    ```

4. **Set up ngrok for HTTPS connection**:
    - **Download ngrok**: Visit the [ngrok download page](https://ngrok.com/download) and download the appropriate version for your operating system.
    - **Install ngrok**: Follow the installation instructions provided on the ngrok download page.
    - **Authenticate ngrok**: Sign up for an ngrok account and get your authentication token from the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken). Run the following command to authenticate ngrok with your token:
        ```bash
        ngrok authtoken YOUR_AUTH_TOKEN
        ```
    - **Start ngrok**: Run ngrok to create an HTTPS tunnel to your local server:
        ```bash
        ./ngrok http 5000
        ```

*IF YOU HOST FROM A DEVICE AND WANT TO USE ON ANOTHER DEVICE, USE NGROK OR ANY OTHER METHODS FOR MAKING HTTPS CONNECTION*
* Mic Can Be Accessed Only Through Localhost or a secure HTTPS connection

## Screenshots 📷📱
![Screenshots ](https://github.com/user-attachments/assets/6c4a9276-cf58-401f-ae62-9b95cc477ca7)

## Contributing 🤝

Feel free to fork this repository and contribute by submitting a pull request. Please ensure your changes are well-documented and tested.

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by SACHINBP1024
