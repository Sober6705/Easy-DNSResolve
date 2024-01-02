import socket
import tkinter as tk
import subprocess
from PIL import Image, ImageTk

def resolve_and_ping():
    domain_name = domain_entry.get()
    try:
        ip_addresses = socket.getaddrinfo(domain_name, None)
        ipv4_addresses = []
        ipv6_addresses = []

        for addr_info in ip_addresses:
            sockaddr = addr_info[-1] 
            ip, port = sockaddr[:2]

            if ':' in ip:
                ipv6_addresses.append(ip)
            else:
                ipv4_addresses.append(ip)

        result_text = ""
        if ipv4_addresses:
            result_text += f"{domain_name} 的 IPv4 地址是:\n{', '.join(ipv4_addresses)}\n"
        if ipv6_addresses:
            result_text += f"{domain_name} 的 IPv6 地址是:\n{', '.join(ipv6_addresses)}\n"

        result_label.config(text=result_text)

        ping_result = subprocess.getoutput(f"ping -n 4 {domain_name}") 
        result_label.config(text=result_text + "\n\nPing测试结果:\n" + ping_result)
    except socket.gaierror:
        result_label.config(text="域名解析失败")

root = tk.Tk()
root.title("DNS Resolve")
root.geometry("400x300")

bg_image = Image.open("b03d63e8a619b64733271b7bbc64797b.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

domain_label = tk.Label(root, text="请输入要解析和Ping测试的域名:")
domain_label.pack(pady=10)
domain_entry = tk.Entry(root)
domain_entry.pack()

resolve_button = tk.Button(root, text="解析和Ping测试", command=resolve_and_ping)
resolve_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()