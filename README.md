# Secret Emoji Communicator v1.0

A simple and private desktop application to encode and decode text messages into a custom set of emojis. Perfect for sending hidden messages in plain sight!

**⚠️ IMPORTANT:** This tool is for fun and educational purposes. The security relies entirely on the secrecy of the `emoji_key.txt` file. Do not use it for highly sensitive information.

---

## 🚀 How it Works

This tool uses a simple substitution cipher, but instead of letters, it substitutes **entire words** with emojis.

1.  **Converter:** You type a normal message (e.g., "hello brother"). The tool replaces each word with a corresponding emoji from a secret key file (e.g., `🦊 🦋`).
2.  **Share:** You can copy and paste this emoji string anywhere (like WhatsApp, Telegram, etc.).
3.  **Resolver:** The receiver pastes the emoji string into their tool (which has the *same* key file). It decodes the emojis back into the original message.

The key to privacy is that the mapping between words and emojis is completely random and stored in a local file (`emoji_key.txt`). Without this file, the emojis are just random symbols.

---

## 📁 File Structure

Before running, make sure your project folder has these files:



