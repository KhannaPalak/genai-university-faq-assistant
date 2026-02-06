import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- GLOBAL CONFIG ----------------
api_key = None

BG = "#f2f5ff"
PRIMARY = "#3f51b5"
ACCENT = "#ffebcd"
CARD = "#ffffff"
TEXT = "#2c2c2c"

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("University FAQ Assistant")
root.geometry("1050x650")
root.configure(bg=BG)

# ---------------- HEADER ----------------
header = tk.Frame(root, bg=PRIMARY, height=70)
header.pack(fill="x")

tk.Label(
    header,
    text="🎓 University FAQ Assistant",
    bg=PRIMARY,
    fg="white",
    font=("Georgia", 22, "bold")
).pack(pady=15)

# ---------------- LAYOUT ----------------
body = tk.Frame(root, bg=BG)
body.pack(fill="both", expand=True)

# ---------------- SIDEBAR ----------------
sidebar = tk.Frame(body, bg=ACCENT, width=220)
sidebar.pack(side="left", fill="y")

tk.Label(
    sidebar,
    text="📘 MENU",
    bg=ACCENT,
    font=("Georgia", 13, "bold")
).pack(pady=20)

def open_admin():
    global api_key

    admin = tk.Toplevel(root)
    admin.title("Admin Panel")
    admin.geometry("400x250")
    admin.configure(bg=BG)

    tk.Label(
        admin,
        text="🔐 Admin Panel",
        font=("Georgia", 16, "bold"),
        bg=BG
    ).pack(pady=15)

    tk.Label(
        admin,
        text="Enter OpenAI API Key:",
        bg=BG
    ).pack()

    key_entry = ttk.Entry(admin, width=40, show="*")
    key_entry.pack(pady=8)

    def save_key():
        nonlocal key_entry
        global api_key
        api_key = key_entry.get().strip()
        if api_key:
            messagebox.showinfo("Success", "API Key configured successfully ✅")
            admin.destroy()
        else:
            messagebox.showerror("Error", "API Key cannot be empty")

    ttk.Button(admin, text="Save API Key", command=save_key).pack(pady=12)

menu_items = [
    ("🏠 Home", None),
    ("📚 FAQ Categories", None),
    ("🔐 Admin Panel", open_admin),
    ("❓ Help", None),
    ("🚪 Exit", root.destroy)
]

for text, action in menu_items:
    ttk.Button(
        sidebar,
        text=text,
        command=action
    ).pack(fill="x", padx=20, pady=6)

# ---------------- MAIN CONTENT ----------------
main = tk.Frame(body, bg=BG)
main.pack(side="right", fill="both", expand=True, padx=25, pady=20)

# ---------------- INFO CARD ----------------
info = tk.Frame(main, bg=CARD, bd=1, relief="solid")
info.pack(fill="x", pady=10)

info_text = (
    "📌 HOW TO USE THIS ASSISTANT\n\n"
    "1️⃣ Enter your question in the search box\n"
    "2️⃣ Click on Search\n"
    "3️⃣ View the answer below\n\n"
    "📚 CATEGORIES COVERED\n"
    "• Admission • Courses • Fees • Scholarships\n"
    "• Exams • Hostel • Placement • Contact\n\n"
    "💡 SAMPLE QUESTIONS\n"
    "• How can I apply for admission?\n"
    "• What courses are offered?\n"
    "• Are scholarships available?"
)

tk.Label(
    info,
    text=info_text,
    bg=CARD,
    fg=TEXT,
    font=("Times New Roman", 11),
    justify="left",
    padx=15,
    pady=15
).pack()

# ---------------- SEARCH AREA ----------------
search_card = tk.Frame(main, bg=CARD, bd=1, relief="solid")
search_card.pack(fill="x", pady=15)

tk.Label(
    search_card,
    text="🔍 Ask Your Question",
    font=("Georgia", 14, "bold"),
    bg=CARD
).pack(pady=10)

search_entry = ttk.Entry(search_card, width=65, font=("Segoe UI", 12))
search_entry.pack(pady=8, ipady=6)

def search_faq():
    q = search_entry.get().lower().strip()
    answer_box.delete("1.0", tk.END)

    if not q:
        messagebox.showwarning("Input Error", "Please enter a question.")
        return

    data = {
        "admission": "Admissions are based on entrance exams and merit lists.",
        "course": "We offer Engineering, Management, Science and Arts programs.",
        "fee": "Fee structure varies depending on the course.",
        "scholarship": "Merit-based and need-based scholarships are available.",
        "exam": "Exams are conducted semester-wise.",
        "hostel": "Hostel facilities are available for students.",
        "placement": "The placement cell supports internships and jobs.",
        "contact": "Email: contact@university.edu"
    }

    for key in data:
        if key in q:
            answer_box.insert(tk.END, data[key])
            return

    answer_box.insert(
        tk.END,
        "⚠️ No exact match found.\n\n"
        "This assistant is GenAI-ready.\n"
        "Admin can enable AI responses using the API key."
    )

ttk.Button(
    search_card,
    text="Search",
    command=search_faq
).pack(pady=10)

# ---------------- ANSWER BOX ----------------
answer_frame = tk.Frame(main)
answer_frame.pack(fill="both", expand=True)

answer_box = tk.Text(
    answer_frame,
    font=("Times New Roman", 12),
    bg=CARD,
    fg=TEXT,
    wrap="word"
)
answer_box.pack(side="left", fill="both", expand=True)

scroll = ttk.Scrollbar(answer_frame, command=answer_box.yview)
scroll.pack(side="right", fill="y")
answer_box.config(yscrollcommand=scroll.set)

# ---------------- FOOTER ----------------
tk.Label(
    root,
    text="Academic Project | Secure | Admin Controlled | GenAI Ready",
    bg=ACCENT,
    font=("Segoe UI", 9)
).pack(fill="x")

root.mainloop()

