import tkinter as tk, random, math

class KeygenApp:
    def __init__(self, root):
        self.root = root
        root.title("Cyberpunk 2077 - License Key Generator")
        root.geometry("800x600")
        root.config(bg='black')
        self.phase = 0
        self.twinkle = 0
        self.particles = []
        self.colors = ['#00ff00', '#00cc00', '#009900', '#006600']

        self.bg = tk.Canvas(root, bg='#000811', highlightthickness=0)
        self.bg.place(relwidth=1, relheight=1)
        self.draw_city()

        self.frame = tk.Frame(root, bg='#001100', relief='raised', bd=3)
        self.frame.place(relx=.5, rely=.5, anchor='center', width=550, height=350)

        self.title = tk.Label(self.frame, text="CYBERPUNK 2077 LICENSE",
                              font=('Courier', 18, 'bold'), fg='#00ff00', bg='#001100')
        self.title.pack(pady=10)

        self.key = tk.StringVar(value="»» WAITING FOR INPUT ««")
        self.key_label = tk.Label(self.frame, textvariable=self.key, font=('Courier', 16, 'bold'),
                                  fg='#00ff00', bg='#000811', relief='groove', bd=3, padx=25, pady=12, width=28)
        self.key_label.pack(pady=10)

        self.btn = tk.Button(self.frame, text="» GENERATE LICENSE KEY «", font=('Courier', 14, 'bold'),
                             bg='#002200', fg='#00ff00', activebackground='#004400',
                             command=self.generate_key)
        self.btn.pack(pady=15)
        self.btn.bind('<Enter>', lambda e: self.btn.config(bg='#003300', fg='#ffffff'))
        self.btn.bind('<Leave>', lambda e: self.btn.config(bg='#002200', fg='#00ff00'))

        self.scan = tk.Canvas(self.frame, width=450, height=6, bg='#000811', highlightthickness=0)
        self.scan.pack(pady=8)

        self.status = tk.StringVar(value="● SYSTEM READY - AWAITING INPUT ●")
        tk.Label(self.frame, textvariable=self.status, font=('Courier', 9, 'bold'),
                 fg='#00ff00', bg='#001100').pack()

        for _ in range(50):
            self.particles.append({'x': random.randint(0,800), 'y': random.randint(0,600),
                                   'speed': random.uniform(0.5,2), 'size': random.randint(1,3),
                                   'color': random.choice(self.colors)})
        self.animate()

    def draw_city(self):
        for i in range(10):
            x, h = i*80, random.randint(160,250)
            self.bg.create_rectangle(x,600-h,x+70,600,fill=random.choice(['#001122','#002233','#001a33','#002244','#001133']),outline='')
            for f in range(5):
                for w in range(3):
                    if random.random()>0.3:
                        self.bg.create_rectangle(x+10+w*20,600-h+20+f*25,x+18+w*20,600-h+32+f*25,fill='#00ff00',outline='')
        for i,t in enumerate(["DATA","NET","CORE","SYS","TECH"]):
            self.bg.create_text(100+i*120,500,text=t,font=('Courier',12,'bold'),fill='#00ff00')

    def generate_key(self):
        n1,n2 = sorted(random.sample(range(1,27),2))
        part1, part3 = f"{n1:02d}", f"{n2:02d}"
        chars = [chr(random.randint(ord('A')+n1-1, ord('A')+n2-1)) for _ in range(7)]
        key = f"{part1} {''.join(chars)} {part3}"
        self.animate_key(key)

    def animate_key(self, key):
        def typer(i=0):
            if i<=len(key):
                self.key.set(key[:i]+("█" if i<len(key) else ""))
                self.root.after(50, typer, i+1)
        self.status.set("● GENERATING SECURE KEY...")
        self.frame.config(bg='#003300')
        self.root.after(150, lambda: typer())
        self.root.after(800, lambda: (self.frame.config(bg='#001100'),
                                      self.key_label.config(bg='#000811', fg='#00ff00'),
                                      self.status.set(f"● KEY ACTIVE: {key} ●"),
                                      self.flash_windows()))

    def flash_windows(self):
        self.bg.delete("flash")
        for _ in range(10):
            x,y=random.randint(0,9)*80+10+random.randint(0,2)*20,600-random.randint(150,250)+20+random.randint(0,4)*25
            self.bg.create_rectangle(x,y,x+8,y+12,fill='#ffffff',tags="flash")
        self.root.after(200, lambda: self.bg.delete("flash"))

    def animate(self):
        self.phase=(self.phase+1)%8; self.twinkle+=1
        self.scan.delete("all")
        for i in range(15):
            if (self.phase+i)%8<4:
                self.scan.create_rectangle(i*30,0,(i+1)*30,6,fill=self.colors[(self.phase+i)%4],outline='')
        self.title.config(fg=f'#00{int(abs(math.sin(self.twinkle*0.1))*100+155):02x}00')
        if self.twinkle%10==0: self.flash_windows()
        self.bg.delete("p")
        for p in self.particles:
            p['y']-=p['speed']
            if p['y']<-10: p.update(y=610,x=random.randint(0,800))
            self.bg.create_oval(p['x'],p['y'],p['x']+p['size'],p['y']+p['size'],fill=p['color'],outline='',tags="p")
        self.status.set(self.status.get().replace("●","○") if self.twinkle%10<5 else self.status.get().replace("○","●"))
        self.root.after(60, self.animate)

if __name__ == "__main__":
    KeygenApp(tk.Tk()).root.mainloop()
