import customtkinter as ctk
import os
import random

# --- App Configuration ---
APP_NAME = "Secret Emoji Communicator"
VERSION = "1.0"
KEY_FILE = "emoji_key.txt"

class EmojiApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title(f"{APP_NAME} v{VERSION}")
        self.geometry("700x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Set Theme to Dark Green ---
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        # --- Load Emoji Key ---
        self.encode_map = {}
        self.decode_map = {}
        self.load_key()

        # --- Main GUI Frame ---
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

        # --- Title ---
        title_label = ctk.CTkLabel(
            self.main_frame,
            text=APP_NAME,
            font=ctk.CTkFont(size=24, weight="bold", slant="italic")
        )
        title_label.grid(row=0, column=0, pady=10)

        # --- Converter Section ---
        converter_frame = ctk.CTkFrame(self.main_frame)
        converter_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew", ipady=10)
        converter_frame.grid_columnconfigure(0, weight=1)

        conv_label = ctk.CTkLabel(
            converter_frame,
            text="1. Convert Text to Emoji",
            font=ctk.CTkFont(size=18, weight="bold", slant="italic")
        )
        conv_label.grid(row=0, column=0, pady=5, padx=10)

        self.text_input = ctk.CTkTextbox(
            converter_frame,
            height=100,
            font=ctk.CTkFont(size=14, slant="italic")
        )
        self.text_input.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        conv_button = ctk.CTkButton(
            converter_frame,
            text="Convert",
            command=self.convert_to_emoji,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        conv_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.emoji_output = ctk.CTkTextbox(
            converter_frame,
            height=100,
            font=ctk.CTkFont(size=14, slant="italic")
        )
        self.emoji_output.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        # --- Resolver Section ---
        resolver_frame = ctk.CTkFrame(self.main_frame)
        resolver_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew", ipady=10)
        resolver_frame.grid_columnconfigure(0, weight=1)

        res_label = ctk.CTkLabel(
            resolver_frame,
            text="2. Resolve Emoji to Text",
            font=ctk.CTkFont(size=18, weight="bold", slant="italic")
        )
        res_label.grid(row=0, column=0, pady=5, padx=10)

        self.emoji_input = ctk.CTkTextbox(
            resolver_frame,
            height=100,
            font=ctk.CTkFont(size=14, slant="italic")
        )
        self.emoji_input.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        res_button = ctk.CTkButton(
            resolver_frame,
            text="Resolve",
            command=self.resolve_to_text,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        res_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.text_output = ctk.CTkTextbox(
            resolver_frame,
            height=100,
            font=ctk.CTkFont(size=14, slant="italic")
        )
        self.text_output.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

    def load_key(self):
        """Loads the word-to-emoji mapping from the key file."""
        if not os.path.exists(KEY_FILE):
            self.show_error(f"Error: Key file '{KEY_FILE}' not found!")
            return

        with open(KEY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    try:
                        word, emoji = line.split('=', 1)
                        self.encode_map[word.lower()] = emoji
                        self.decode_map[emoji] = word
                    except ValueError:
                        print(f"Skipping malformed line: {line}")

    def add_word_to_key(self, word, emoji):
        """Adds a new word-emoji pair to the key file and maps."""
        with open(KEY_FILE, "a", encoding="utf-8") as f:
            f.write(f"\n{word}={emoji}")
        
        self.encode_map[word] = emoji
        self.decode_map[emoji] = word
        print(f"Added new mapping: {word} -> {emoji}")

    def convert_to_emoji(self):
        """Converts text from the input box to emojis, auto-generating new ones."""
        text = self.text_input.get("1.0", "end-1c").lower()
        words = text.split()
        emoji_result = []

        # A large list of random emojis to pick from
            # A large list of random emojis to pick from
        random_emojis = ["🦜","🦢","🦩","🦚","🦃","🐓","🦤","🦝","🦨","🦡","🦦","🦥","🐁","🐀","🦔","🐇","🐿️","🦫","🦎","🐊","🐢","🐍","🐲","🐉","🦕","🦖","🦭","🐙","🦑","🦐","🦞","🦀","🐡","🐠","🐟","🐬","🐳","🐋","🦈","🐅","🐆","🦄","🦓","🦌","🦬","🐮","🦏","🦛","🐘","🦣","🦒","🐪","🐫","🦘","🦙","🐐","🐏","🐑","🐎","🐖","🐄","🐂","🐃","🐁","🐀","🐇","🐿️","🦫","🦔","🐾","🐉","🐲","🦕","🦖","🦢","🦜","🦩","🦚","🦃","🐓","🦤","🦝","🦨","🦡","🦦","🦥","🐁","🐀","🦔","🐇","🐿️","🦫","🦎","🐊","🐢","🐍","🦭","🐙","🦑","🦐","🦞","🦀","🐡","🐠","🐟","🐬","🐳","🐋","🦈","🐅","🐆","🦄","🦓","🦌","🦬","🐮","🦏","🦛","🐘","🦣","🦒","🐪","🐫","🦘","🦙","🐐","🐏","🐑","🐎","🐖","🐄","🐂","🐃","🐁","🐀","🐇","🐿️","🦫","🦔","🐾","🐉","🐲","🦕","🦖","🦢","🦜","🦩","🦚","🦃","🐓","🦤","🦝","🦨","🦡","🦦","🦥","🐁","🐀","🦔","🐇","🐿️","🦫","🦎","🐊","🐢","🐍","🦭","🐙","🦑","🦐","🦞","🦀","🐡","🐠","🐟","🐬","🐳","🐋","🦈","🐅","🐆","🦄","🦓","🦌","🦬","🐮","🦏","🦛","🐘","🦣","🦒","🐪","🐫","🦘","🦙","🐐","🐏","🐑","🐎","🐖","🐄","🐂","🐃","🐁","🐀","🐇","🐿️","🦫","🦔","🐾","🐉","🐲","🦕","🦖","🦢","🦜","🦩","🦚","🦃","🐓","🦤","🦝","🦨","🦡","🦦","🦥","🐁","🐀","🦔","🐇","🐿️","🦫","🦎","🐊","🐢","🐍","🦭","🐙","🦑","🦐","🦞","🦀","🐡","🐠","🐟","🐬","🐳","🐋","🦈","🐅","🐆","🦄","🦓","🦌","🦬","🐮","🦏","🦛","🐘","🦣","🦒","🐪","🐫","🦘","🦙","🐐","🐏","🐑","🐎","🐖","🐄","🐂","🐃","🐁","🐀","🐇","🐿️","🦫","🦔","🐾","🐉","🐲","🦕","🦖","🦢","🦜","🦩","🦚","🦃","🐓","🦤","🦝","🦨","🦡","🦦","🦥","🐁","🐀","🦔","🐇","🐿️","🦫","🦎","🐊","🐢","🐍","🦭","🐙","🦑","🦐","🦞","🦀","🐡","🐠","🐟","🐬","🐳","🐋","🦈","🐅","🐆","🦄","🦓","🦌","🦬","🐮","🦏","🦛","🐘","🦣","🦒","🐪","🐫","🦘","🦙","🐐","🐏","🐑","🐎","🐖","🐄","🐂","🐃","🐁","🐀","🐇","🐿️","🦫","🦔","🐾","🐉","🐲","🦕","🦖","🦢","🦜","🦩","🦚","🦃","🐓","🦤","🦝","🦨","🦡","🦦","🦥","🐁","🐀","🦔","🐇","🐿️","🦫","🦎","🐊","🐢","🐍","🦭","🐙","🦑","🦐","🦞","🦀","🐡","🐠","🐟","🐬","🐳","🐋","🦈","🐅","🐆","🦄","🦓","🦌","🦬","🐮","🦏","🦛","🐘","🦣","🦒","🐪","🐫","🦘","🦙","🐐","🐏","🐑","🐎","🐖","🐄","🐂","🐃","🐁","🐀","🐇","🐿️","🦫","🦔","🐾","🐉","🐲","🦕","🦖","🦢","🦜","🦩","🦚","🦃","🐓","🦤","🦝","🦨","🦡","🦦","🦥","🐁","🐀","🦔"]
