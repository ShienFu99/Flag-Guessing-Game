#Imports
import customtkinter
import sys
from PIL import Image
import os
from functools import partial
from random import shuffle


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    width = 1000
    height = 850
    flag_counter = 1

    country_flags = [
        {"country_name": "afghanistan", "img_file_name": "af.png"},
        {"country_name": "albania", "img_file_name": "al.png"},
        {"country_name": "algeria", "img_file_name": "dz.png"},
        {"country_name": "andorra", "img_file_name": "ad.png"},
        {"country_name": "angola", "img_file_name": "ao.png"},
        {"country_name": "antigua and barbuda", "img_file_name": "ag.png"},
        {"country_name": "argentina", "img_file_name": "ar.png"},
        {"country_name": "armenia", "img_file_name": "am.png"},
        {"country_name": "australia", "img_file_name": "au.png"},
        {"country_name": "austria", "img_file_name": "at.png"},
        {"country_name": "azerbaijan", "img_file_name": "az.png"},
        {"country_name": "bahamas", "img_file_name": "bs.png"},
        {"country_name": "bahrain", "img_file_name": "bh.png"},
        {"country_name": "bangladesh", "img_file_name": "bd.png"},
        {"country_name": "barbados", "img_file_name": "bb.png"},
        {"country_name": "belarus", "img_file_name": "by.png"},
        {"country_name": "belgium", "img_file_name": "be.png"},
        {"country_name": "belize", "img_file_name": "bz.png"},
        {"country_name": "benin", "img_file_name": "bj.png"},
        {"country_name": "bhutan", "img_file_name": "bt.png"},
        {"country_name": "bolivia", "img_file_name": "bo.png"},
        {"country_name": "bosnia and herzegovina", "img_file_name": "ba.png"},
        {"country_name": "botswana", "img_file_name": "bw.png"},
        {"country_name": "brazil", "img_file_name": "br.png"},
        {"country_name": "brunei", "img_file_name": "bn.png"},
        {"country_name": "bulgaria", "img_file_name": "bg.png"},
        {"country_name": "burkina faso", "img_file_name": "bf.png"},
        {"country_name": "burundi", "img_file_name": "bi.png"},
        {"country_name": "côte d'ivoire", "img_file_name": "ci.png"},
        {"country_name": "cabo verde", "img_file_name": "cv.png"},
        {"country_name": "cambodia", "img_file_name": "kh.png"},
        {"country_name": "cameroon", "img_file_name": "cm.png"},
        {"country_name": "canada", "img_file_name": "ca.png"},
        {"country_name": "central african republic", "img_file_name": "cf.png"},
        {"country_name": "chad", "img_file_name": "td.png"},
        {"country_name": "chile", "img_file_name": "cl.png"},
        {"country_name": "china", "img_file_name": "cn.png"},
        {"country_name": "colombia", "img_file_name": "co.png"},
        {"country_name": "comoros", "img_file_name": "km.png"},
        {"country_name": "congo", "img_file_name": "cg.png"},
        {"country_name": "costa rica", "img_file_name": "cr.png"},
        {"country_name": "croatia", "img_file_name": "hr.png"},
        {"country_name": "cuba", "img_file_name": "cu.png"},
        {"country_name": "cyprus", "img_file_name": "cy.png"},
        {"country_name": "czechia", "img_file_name": "cz.png"},
        {"country_name": "denmark", "img_file_name": "dk.png"},
        {"country_name": "djibouti", "img_file_name": "dj.png"},
        {"country_name": "dominica", "img_file_name": "dm.png"},
        {"country_name": "dominican republic", "img_file_name": "do.png"},
        {"country_name": "democratic republic of the congo", "img_file_name": "cd.png"},
        {"country_name": "ecuador", "img_file_name": "ec.png"},
        {"country_name": "egypt", "img_file_name": "eg.png"},
        {"country_name": "el salvador", "img_file_name": "sv.png"},
        {"country_name": "equatorial guinea", "img_file_name": "gq.png"},
        {"country_name": "eritrea", "img_file_name": "er.png"},
        {"country_name": "estonia", "img_file_name": "ee.png"},
        {"country_name": "eswatini", "img_file_name": "sz.png"},
        {"country_name": "ethiopia", "img_file_name": "et.png"},
        {"country_name": "fiji", "img_file_name": "fj.png"},
        {"country_name": "finland", "img_file_name": "fi.png"},
        {"country_name": "france", "img_file_name": "fr.png"},
        {"country_name": "gabon", "img_file_name": "ga.png"},
        {"country_name": "gambia", "img_file_name": "gm.png"},
        {"country_name": "georgia", "img_file_name": "ge.png"},
        {"country_name": "germany", "img_file_name": "de.png"},
        {"country_name": "ghana", "img_file_name": "gh.png"},
        {"country_name": "greece", "img_file_name": "gr.png"},
        {"country_name": "grenada", "img_file_name": "gd.png"},
        {"country_name": "guatemala", "img_file_name": "gt.png"},
        {"country_name": "guinea", "img_file_name": "gn.png"},
        {"country_name": "guinea-bissau", "img_file_name": "gw.png"},
        {"country_name": "guyana", "img_file_name": "gy.png"},
        {"country_name": "haiti", "img_file_name": "ht.png"},
        {"country_name": "holy see", "img_file_name": "va.png"},
        {"country_name": "honduras", "img_file_name": "hn.png"},
        {"country_name": "hungary", "img_file_name": "hu.png"},
        {"country_name": "iceland", "img_file_name": "is.png"},
        {"country_name": "india", "img_file_name": "in.png"},
        {"country_name": "indonesia", "img_file_name": "id.png"},
        {"country_name": "iran", "img_file_name": "ir.png"},
        {"country_name": "iraq", "img_file_name": "iq.png"},
        {"country_name": "ireland", "img_file_name": "ie.png"},
        {"country_name": "israel", "img_file_name": "il.png"},
        {"country_name": "italy", "img_file_name": "it.png"},
        {"country_name": "jamaica", "img_file_name": "jm.png"},
        {"country_name": "japan", "img_file_name": "jp.png"},
        {"country_name": "jordan", "img_file_name": "jo.png"},
        {"country_name": "kazakhstan", "img_file_name": "kz.png"},
        {"country_name": "kenya", "img_file_name": "ke.png"},
        {"country_name": "kiribati", "img_file_name": "ki.png"},
        {"country_name": "kuwait", "img_file_name": "kw.png"},
        {"country_name": "kyrgyzstan", "img_file_name": "kg.png"},
        {"country_name": "laos", "img_file_name": "la.png"},
        {"country_name": "latvia", "img_file_name": "lv.png"},
        {"country_name": "lebanon", "img_file_name": "lb.png"},
        {"country_name": "lesotho", "img_file_name": "ls.png"},
        {"country_name": "liberia", "img_file_name": "lr.png"},
        {"country_name": "libya", "img_file_name": "ly.png"},
        {"country_name": "liechtenstein", "img_file_name": "li.png"},
        {"country_name": "lithuania", "img_file_name": "lt.png"},
        {"country_name": "luxembourg", "img_file_name": "lu.png"},
        {"country_name": "madagascar", "img_file_name": "mg.png"},
        {"country_name": "malawi", "img_file_name": "mw.png"},
        {"country_name": "malaysia", "img_file_name": "my.png"},
        {"country_name": "maldives", "img_file_name": "mv.png"},
        {"country_name": "mali", "img_file_name": "ml.png"},
        {"country_name": "malta", "img_file_name": "mt.png"},
        {"country_name": "marshall islands", "img_file_name": "mh.png"},
        {"country_name": "mauritania", "img_file_name": "mr.png"},
        {"country_name": "mauritius", "img_file_name": "mu.png"},
        {"country_name": "mexico", "img_file_name": "mx.png"},
        {"country_name": "micronesia", "img_file_name": "fm.png"},
        {"country_name": "moldova", "img_file_name": "md.png"},
        {"country_name": "monaco", "img_file_name": "mc.png"},
        {"country_name": "mongolia", "img_file_name": "mn.png"},
        {"country_name": "montenegro", "img_file_name": "me.png"},
        {"country_name": "morocco", "img_file_name": "ma.png"},
        {"country_name": "mozambique", "img_file_name": "mz.png"},
        {"country_name": "myanmar", "img_file_name": "mm.png"},
        {"country_name": "namibia", "img_file_name": "na.png"},
        {"country_name": "nauru", "img_file_name": "nr.png"},
        {"country_name": "nepal", "img_file_name": "np.png"},
        {"country_name": "netherlands", "img_file_name": "nl.png"},
        {"country_name": "new zealand", "img_file_name": "nz.png"},
        {"country_name": "nicaragua", "img_file_name": "ni.png"},
        {"country_name": "niger", "img_file_name": "ne.png"},
        {"country_name": "nigeria", "img_file_name": "ng.png"},
        {"country_name": "north korea", "img_file_name": "kp.png"},
        {"country_name": "north macedonia", "img_file_name": "mk.png"},
        {"country_name": "norway", "img_file_name": "no.png"},
        {"country_name": "oman", "img_file_name": "om.png"},
        {"country_name": "pakistan", "img_file_name": "pk.png"},
        {"country_name": "palau", "img_file_name": "pw.png"},
        {"country_name": "panama", "img_file_name": "pa.png"},
        {"country_name": "papua new guinea", "img_file_name": "pg.png"},
        {"country_name": "paraguay", "img_file_name": "py.png"},
        {"country_name": "peru", "img_file_name": "pe.png"},
        {"country_name": "philippines", "img_file_name": "ph.png"},
        {"country_name": "poland", "img_file_name": "pl.png"},
        {"country_name": "portugal", "img_file_name": "pt.png"},
        {"country_name": "qatar", "img_file_name": "qa.png"},
        {"country_name": "romania", "img_file_name": "ro.png"},
        {"country_name": "russia", "img_file_name": "ru.png"},
        {"country_name": "rwanda", "img_file_name": "rw.png"},
        {"country_name": "saint kitts and nevis", "img_file_name": "kn.png"},
        {"country_name": "saint lucia", "img_file_name": "lc.png"},
        {"country_name": "samoa", "img_file_name": "ws.png"},
        {"country_name": "san marino", "img_file_name": "sm.png"},
        {"country_name": "sao tome and principe", "img_file_name": "st.png"},
        {"country_name": "saudi arabia", "img_file_name": "sa.png"},
        {"country_name": "senegal", "img_file_name": "sn.png"},
        {"country_name": "serbia", "img_file_name": "rs.png"},
        {"country_name": "seychelles", "img_file_name": "sc.png"},
        {"country_name": "sierra leone", "img_file_name": "sl.png"},
        {"country_name": "singapore", "img_file_name": "sg.png"},
        {"country_name": "slovakia", "img_file_name": "sk.png"},
        {"country_name": "slovenia", "img_file_name": "si.png"},
        {"country_name": "solomon islands", "img_file_name": "sb.png"},
        {"country_name": "somalia", "img_file_name": "so.png"},
        {"country_name": "south africa", "img_file_name": "za.png"},
        {"country_name": "south korea", "img_file_name": "kr.png"},
        {"country_name": "south sudan", "img_file_name": "ss.png"},
        {"country_name": "spain", "img_file_name": "es.png"},
        {"country_name": "sri lanka", "img_file_name": "lk.png"},
        {"country_name": "st. vincent grenadines", "img_file_name": "vc.png"},
        {"country_name": "state of palestine", "img_file_name": "ps.png"},
        {"country_name": "sudan", "img_file_name": "sd.png"},
        {"country_name": "suriname", "img_file_name": "sr.png"},
        {"country_name": "sweden", "img_file_name": "se.png"},
        {"country_name": "switzerland", "img_file_name": "ch.png"},
        {"country_name": "syria", "img_file_name": "sy.png"},
        {"country_name": "tajikistan", "img_file_name": "tj.png"},
        {"country_name": "tanzania", "img_file_name": "tz.png"},
        {"country_name": "thailand", "img_file_name": "th.png"},
        {"country_name": "timor-leste", "img_file_name": "tl.png"},
        {"country_name": "togo", "img_file_name": "tg.png"},
        {"country_name": "tonga", "img_file_name": "to.png"},
        {"country_name": "trinidad and tobago", "img_file_name": "tt.png"},
        {"country_name": "tunisia", "img_file_name": "tn.png"},
        {"country_name": "turkey", "img_file_name": "tr.png"},
        {"country_name": "turkmenistan", "img_file_name": "tm.png"},
        {"country_name": "tuvalu", "img_file_name": "tv.png"},
        {"country_name": "united arab emirates", "img_file_name": "ae.png"},
        {"country_name": "united kingdom", "img_file_name": "gb.png"},
        {"country_name": "united states", "img_file_name": "us.png"},
        {"country_name": "uganda", "img_file_name": "ug.png"},
        {"country_name": "ukraine", "img_file_name": "ua.png"},
        {"country_name": "uruguay", "img_file_name": "uy.png"},
        {"country_name": "uzbekistan", "img_file_name": "uz.png"},
        {"country_name": "vanuatu", "img_file_name": "vu.png"},
        {"country_name": "venezuela", "img_file_name": "ve.png"},
        {"country_name": "vietnam", "img_file_name": "vn.png"},
        {"country_name": "yemen", "img_file_name": "ye.png"},
        {"country_name": "zambia", "img_file_name": "zm.png"},
        {"country_name": "zimbabwe", "img_file_name": "zw.png"}
    ]

    shuffle(country_flags)

    def __init__(self):
        super().__init__()

        # configure window
        self.title(sys.argv[0])
        self.geometry(f"{self.width}x{self.height}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.background_frame = customtkinter.CTkFrame(self, fg_color="cyan", corner_radius=0)
        self.background_frame.grid(padx=0, pady=0, sticky="nsew")
        self.background_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.background_frame.grid_columnconfigure(0, weight=1)

        self.flag_counter_label = customtkinter.CTkLabel(self.background_frame, text=f"Flag {self.flag_counter}", font=("arial", 32))
        self.flag_counter_label.grid(row=1, column=0, padx=20, pady=20)

        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "country_flag_images")

        self.current_flag = self.country_flags[0]["img_file_name"]

        self.flag_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, self.current_flag)), size=(400, 240))

        self.image_label = customtkinter.CTkLabel(self.background_frame, text="", image=self.flag_image)
        self.image_label.grid(row=2, column=0, padx=20, pady=20)

        self.next_button = customtkinter.CTkButton(self.background_frame, text="Next", font=("arial", 32), width=400, height=80,
                                                   command=partial(self.next_image, self.country_flags))
        self.next_button.grid(row=3, column=0, padx=20, pady=20)


    def next_image(self, country_flags):

        flags_match = False

        for d in country_flags:
            if d["img_file_name"] == self.current_flag:
                flags_match = True
                continue
            if flags_match:
                self.current_flag = d["img_file_name"]
                self.flag_counter += 1
                break

        self.flag_counter_label.configure(text=f"Flag {self.flag_counter}")

        self.flag_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, self.current_flag)), size=(400, 240))

        self.image_label = customtkinter.CTkLabel(self.background_frame, text="", image=self.flag_image)
        self.image_label.grid(row=2, column=0, padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()


#customtkinter.set_appearance_mode(new_appearance_mode)
#Time elapsed: 171:14.50
