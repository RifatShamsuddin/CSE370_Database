def convert_to_absolute_url(link):
    base_url = "https://en.wikipedia.org"

    # Extract the relative URL from the link
    relative_url_start = link.find('href="') + len('href="')
    relative_url_end = link.find('"', relative_url_start)
    relative_url = link[relative_url_start:relative_url_end]

    # Combine the relative URL with the base URL
    absolute_url = base_url + relative_url

    return absolute_url


def process_links(links_string):
    links_list = links_string.split("</li>")
    absolute_urls = []
    for link in links_list:
        if "<a href" in link:
            absolute_url = convert_to_absolute_url(link)
            absolute_urls.append(absolute_url)

    return absolute_urls


# Test with the provided links string

links_string = '''<ul><li><a href="/wiki/3Hz" title="3Hz">3Hz</a></li>
<li><a href="/wiki/A.C.G.T" title="A.C.G.T">A.C.G.T</a></li>
<li><a href="/wiki/A.P.P.P." title="A.P.P.P.">A.P.P.P.</a></li>
<li><a href="/wiki/Anime_International_Company" title="Anime International Company">AIC</a></li>
<li><a href="/wiki/Ajia-do_Animation_Works" title="Ajia-do Animation Works">Ajia-do Animation Works</a></li>
<li><a href="/wiki/Arvo_Animation" title="Arvo Animation">Arvo Animation</a></li>
<li><a href="/wiki/Asahi_Production" title="Asahi Production">Asahi Production</a></li>
<li><a href="/wiki/Ashi_Productions" title="Ashi Productions">Ashi Productions</a></li>
<li><a href="/wiki/Asread" title="Asread">Asread</a></li>
<li><a href="/wiki/AXsiZ" title="AXsiZ">AXsiZ</a></li>
<li><a href="/wiki/Bibury_Animation_Studios" title="Bibury Animation Studios">Bibury Animation Studios</a></li>
<li><a href="/wiki/Bones_(studio)" title="Bones (studio)">Bones</a></li>
<li><a href="/wiki/Brain%27s_Base" title="Brain&#39;s Base">Brain's Base</a></li>
<li><a href="/wiki/Bridge_(studio)" title="Bridge (studio)">Bridge</a></li>
<li><a href="/wiki/C-Station" title="C-Station">C-Station</a></li>
<li><a href="/wiki/C2C_(studio)" title="C2C (studio)">C2C</a></li>
<li><a href="/wiki/Cloud_Hearts" title="Cloud Hearts">Cloud Hearts</a></li>
<li><a href="/wiki/CoMix_Wave_Films" title="CoMix Wave Films">CoMix Wave Films</a></li>
<li><a href="/wiki/Creators_in_Pack" title="Creators in Pack">Creators in Pack</a></li>
<li><a href="/wiki/Diomed%C3%A9a" title="Diomedéa">Diomedéa</a></li>
<li><a href="/wiki/Doga_Kobo" title="Doga Kobo">Doga Kobo</a></li>
<li><a href="/wiki/Egg_Firm" title="Egg Firm">Egg Firm</a></li>
<li><a href="/wiki/Eight_Bit_(studio)" title="Eight Bit (studio)">Eight Bit</a></li>
<li><a href="/wiki/Ekachi_Epilka" title="Ekachi Epilka">Ekachi Epilka</a></li>
<li><a href="/wiki/Haoliners_Animation_League" title="Haoliners Animation League">Emon</a></li>
<li><a href="/wiki/EMT_Squared" title="EMT Squared">EMT Squared</a></li>
<li><a href="/wiki/Encourage_Films" title="Encourage Films">Encourage Films</a></li>
<li><a href="/wiki/Ezo%27la" title="Ezo&#39;la">Ezo'la</a></li>
<li><a href="/wiki/Felix_Film" title="Felix Film">Felix Film</a></li>
<li><a href="/wiki/Frontier_Works" title="Frontier Works">Frontier Works</a></li>
<li><a href="/wiki/Gainax" title="Gainax">Gainax</a></li>
<li><a href="/wiki/Gallop_(studio)" title="Gallop (studio)">Gallop</a></li>
<li><a href="/wiki/Genco" title="Genco">Genco</a></li>
<li><a href="/wiki/Gathering_(animation_studio)" title="Gathering (animation studio)">Gathering</a></li>
<li><a href="/wiki/G%26G_Entertainment" title="G&amp;G Entertainment">G&amp;G Direction</a></li>
<li><a href="/wiki/GoHands" title="GoHands">GoHands</a></li>
<li><a href="/wiki/Grizzly_(studio)" title="Grizzly (studio)">Grizzly</a></li>
<li><a href="/wiki/Hoods_Entertainment" title="Hoods Entertainment">Hoods Entertainment</a></li>
<li><a href="/wiki/Imagin_(studio)" title="Imagin (studio)">Imagin</a></li>
<li><a href="/wiki/J.C.Staff" title="J.C.Staff">J.C.Staff</a></li>
<li><a href="/wiki/Khara_(studio)" title="Khara (studio)">Khara</a></li>
<li><a href="/wiki/Kinema_Citrus" title="Kinema Citrus">Kinema Citrus</a></li>
<li><a href="/wiki/Kyoto_Animation" title="Kyoto Animation">Kyoto Animation</a></li>
<li><a href="/wiki/Lapin_Track" title="Lapin Track">Lapin Track</a></li>
<li><a href="/wiki/Lesprit" title="Lesprit">Lesprit</a></li>
<li><a href="/wiki/Magic_Bus_(studio)" title="Magic Bus (studio)">Magic Bus</a></li>
<li><a href="/wiki/Maho_Film" title="Maho Film">Maho Film</a></li>
<li><a href="/wiki/MAPPA" title="MAPPA">MAPPA</a></li>
<li><a href="/wiki/Marvelous_(company)" title="Marvelous (company)">Marvelous</a></li>
<li><a href="/wiki/Movic" title="Movic">Movic</a></li>
<li><a href="/wiki/Millepensee" title="Millepensee">Millepensee</a></li>
<li><a href="/wiki/NAZ_(studio)" class="mw-redirect" title="NAZ (studio)">NAZ</a></li>
<li><a href="/wiki/Nexus_(animation_studio)" title="Nexus (animation studio)">Nexus</a></li>
<li><a href="/wiki/Nippon_Animation" title="Nippon Animation">Nippon Animation</a></li>
<li><a href="/wiki/Nomad_(company)" title="Nomad (company)">Nomad</a></li>
<li><a href="/wiki/NUT_(studio)" title="NUT (studio)">NUT</a></li>
<li><a href="/wiki/Odessa_Entertainment" title="Odessa Entertainment">Odessa Entertainment</a></li>
<li><a href="/wiki/Oh!_Production" title="Oh! Production">Oh! Production</a></li>
<li><a href="/wiki/Okuruto_Noboru" title="Okuruto Noboru">Okuruto Noboru</a></li>
<li><a href="/wiki/Orange_(animation_studio)" title="Orange (animation studio)">Orange</a></li>
<li><a href="/wiki/P.A._Works" title="P.A. Works">P.A. Works</a></li>
<li><a href="/wiki/Passione_(company)" title="Passione (company)">Passione</a></li>
<li><a href="/wiki/Pierrot_(company)" title="Pierrot (company)">Pierrot</a>
<ul><li><a href="/wiki/Studio_Signpost" title="Studio Signpost">Studio Signpost</a></li></ul></li>
<li><a href="/wiki/Pine_Jam" title="Pine Jam">Pine Jam</a></li>
<li><a href="/wiki/Platinum_Vision" title="Platinum Vision">Platinum Vision</a></li>
<li><a href="/wiki/Polygon_Pictures" title="Polygon Pictures">Polygon Pictures</a></li>
<li><a href="/wiki/Project_No.9" title="Project No.9">Project No.9</a></li>
<li><a href="/wiki/Satelight" title="Satelight">Satelight</a></li>
<li><a href="/wiki/Science_Saru" title="Science Saru">Science Saru</a></li>
<li><a href="/wiki/Seven_(animation_studio)" title="Seven (animation studio)">Seven</a></li>
<li><a href="/wiki/Shaft_(company)" title="Shaft (company)">Shaft</a></li>
<li><a href="/wiki/Shirogumi" title="Shirogumi">Shirogumi</a></li>
<li><a href="/wiki/Shuka_(studio)" title="Shuka (studio)">Shuka</a></li>
<li><a href="/wiki/Sola_Digital_Arts" title="Sola Digital Arts">Sola Digital Arts</a></li>
<li><a href="/wiki/Studio_4%C2%B0C" title="Studio 4°C">Studio 4°C</a></li>
<li><a href="/wiki/Studio_A-Cat" title="Studio A-Cat">Studio A-Cat</a></li>
<li><a href="/wiki/Studio_Blanc" title="Studio Blanc">Studio Blanc</a></li>
<li><a href="/wiki/Studio_Chizu" title="Studio Chizu">Studio Chizu</a></li>
<li><a href="/wiki/Studio_Comet" title="Studio Comet">Studio Comet</a></li>
<li><a href="/wiki/Studio_Deen" title="Studio Deen">Studio Deen</a></li>
<li><a href="/wiki/Studio_Flad" title="Studio Flad">Studio Flad</a></li>
<li><a href="/wiki/Studio_Ghibli" title="Studio Ghibli">Studio Ghibli</a></li>
<li><a href="/wiki/Studio_Gokumi" title="Studio Gokumi">Studio Gokumi</a></li>
<li><a href="/wiki/Studio_Nue" title="Studio Nue">Studio Nue</a></li>
<li><a href="/wiki/Studio_Palette" title="Studio Palette">Studio Palette</a></li>
<li><a href="/wiki/Studio_Ponoc" title="Studio Ponoc">Studio Ponoc</a></li>
<li><a href="/wiki/Studio_Puyukai" title="Studio Puyukai">Studio Puyukai</a></li>
<li><a href="/wiki/Studio_VOLN" title="Studio VOLN">Studio VOLN</a></li>
<li><a href="/wiki/Tezuka_Productions" title="Tezuka Productions">Tezuka Productions</a></li>
<li><a href="/wiki/TNK_(company)" title="TNK (company)">TNK</a></li>
<li><a href="/wiki/Troyca" title="Troyca">Troyca</a></li>
<li><a href="/wiki/Typhoon_Graphics" title="Typhoon Graphics">Typhoon Graphics</a></li>
<li><a href="/wiki/Ufotable" title="Ufotable">Ufotable</a></li>
<li><a href="/wiki/White_Fox" title="White Fox">White Fox</a></li>
<li><a href="/wiki/Wolfsbane_(animation_studio)" title="Wolfsbane (animation studio)">Wolfsbane</a></li>
<li><a href="/wiki/Yokohama_Animation_Laboratory" title="Yokohama Animation Laboratory">Yokohama Animation Laboratory</a></li>
<li><a href="/wiki/Zero-G_(studio)" title="Zero-G (studio)">Zero-G</a></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Non-independent</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Asahi_Broadcasting_Corporation" title="Asahi Broadcasting Corporation">Asahi Broadcasting Corporation</a>
<ul><li><a href="/wiki/DLE_(company)" title="DLE (company)">DLE</a></li>
<li><a href="/wiki/Silver_Link" title="Silver Link">Silver Link</a>
<ul><li><a href="/wiki/Connect_(studio)" title="Connect (studio)">Connect</a></li></ul></li></ul></li>
<li><a href="/wiki/Asatsu-DK" title="Asatsu-DK">Asatsu-DK</a>
<ul><li><a href="/wiki/Eiken_(studio)" title="Eiken (studio)">Eiken</a></li>
<li><a href="/wiki/Gonzo_(company)" title="Gonzo (company)">Gonzo</a></li>
<li><a href="/wiki/Nihon_Ad_Systems" title="Nihon Ad Systems">NAS</a></li>
<li><a href="/wiki/Studio_Kai" title="Studio Kai">Studio Kai</a></li></ul></li>
<li><a href="/wiki/Bandai_Namco_Holdings" title="Bandai Namco Holdings">Bandai Namco</a>
<ul><li><a href="/wiki/Bandai_Namco_Arts" class="mw-redirect" title="Bandai Namco Arts">Arts</a>
<ul><li><a href="/wiki/Actas" title="Actas">Actas</a></li></ul></li>
<li><a href="/wiki/Bandai_Namco_Filmworks" title="Bandai Namco Filmworks">Filmworks</a>
<ul><li><a href="/wiki/Bandai_Namco_Pictures" title="Bandai Namco Pictures">Pictures</a></li>
<li><a href="/wiki/Studio_Mother" title="Studio Mother">Studio Mother</a></li></ul></li>
<li><a href="/wiki/Happinet" title="Happinet">Happinet</a></li></ul></li>
<li><a href="/wiki/CyberAgent" title="CyberAgent">CyberAgent</a>
<ul><li><a href="/wiki/Cygames" title="Cygames">Cygames</a>
<ul><li><a href="/wiki/CygamesPictures" title="CygamesPictures">CygamesPictures</a></li></ul></li></ul></li>
<li><a href="/wiki/Digital_Frontier" title="Digital Frontier">Digital Frontier</a>
<ul><li><a href="/wiki/GEMBA_(studio)" title="GEMBA (studio)">GEMBA</a></li></ul></li>
<li><a href="/wiki/Fanworks_(animation_studio)" title="Fanworks (animation studio)">Fanworks</a></li>
<li><a href="/wiki/Feel_(animation_studio)" title="Feel (animation studio)">Feel</a></li>
<li><a href="/wiki/Fuji_TV" class="mw-redirect" title="Fuji TV">Fuji TV</a>
<ul><li><a href="/wiki/Blue_Lynx" title="Blue Lynx">Blue Lynx</a></li>
<li><a href="/wiki/David_Production" title="David Production">David Production</a></li></ul></li>
<li><a href="/wiki/Gaina_(company)" title="Gaina (company)">Gaina</a></li>
<li><a href="/wiki/Geek_Pictures" title="Geek Pictures">Geek Pictures</a>
<ul><li><a href="/wiki/Geek_Toys" title="Geek Toys">Geek Toys</a></li></ul></li>
<li><a href="/wiki/Graphinica" title="Graphinica">Graphinica</a>
<ul><li><a href="/wiki/Yumeta_Company" title="Yumeta Company">Yumeta Company</a></li></ul></li>
<li><a href="/wiki/IG_Port" title="IG Port">IG Port</a>
<ul><li><a href="/wiki/Production_I.G" title="Production I.G">Production I.G</a></li>
<li><a href="/wiki/Signal.MD" title="Signal.MD">Signal.MD</a></li>
<li><a href="/wiki/Wit_Studio" title="Wit Studio">Wit Studio</a></li></ul></li>
<li><a href="/wiki/Imagica" title="Imagica">Imagica</a>
<ul><li><a href="/wiki/OLM,_Inc." title="OLM, Inc.">OLM</a></li>
<li><a href="/wiki/Robot_Communications" title="Robot Communications">Robot Communications</a></li></ul></li>
<li><a href="/wiki/Kadokawa_Corporation" title="Kadokawa Corporation">Kadokawa Corporation</a>
<ul><li><a href="/wiki/Dwango_(company)" title="Dwango (company)">Dwango</a></li>
<li><a href="/wiki/ENGI" title="ENGI">ENGI</a></li></ul></li>
<li><a href="/wiki/Nintendo" title="Nintendo">Nintendo</a>
<ul><li><a href="/wiki/Nintendo_Pictures" title="Nintendo Pictures">Nintendo Pictures</a></li></ul></li>
<li><a href="/wiki/Nippon_TV" title="Nippon TV">Nippon TV</a>
<ul><li><a href="/wiki/Madhouse_(company)" title="Madhouse (company)">Madhouse</a></li>
<li><a href="/wiki/Tatsunoko_Production" title="Tatsunoko Production">Tatsunoko Production</a></li></ul></li>
<li><a href="/wiki/Sega_Sammy_Holdings" title="Sega Sammy Holdings">Sega Sammy Holdings</a>
<ul><li><a href="/wiki/TMS_Entertainment" title="TMS Entertainment">TMS Entertainment</a>
<ul><li><a href="/wiki/Marza_Animation_Planet" title="Marza Animation Planet">Marza Animation Planet</a></li>
<li><a href="/wiki/Telecom_Animation_Film" title="Telecom Animation Film">Telecom Animation Film</a></li></ul></li></ul></li>
<li><a href="/wiki/Sony_Music_Entertainment_Japan" title="Sony Music Entertainment Japan">Sony Music Entertainment Japan</a>
<ul><li><a href="/wiki/Aniplex" title="Aniplex">Aniplex</a>
<ul><li><a href="/wiki/A-1_Pictures" title="A-1 Pictures">A-1 Pictures</a></li>
<li><a href="/wiki/CloverWorks" title="CloverWorks">CloverWorks</a></li></ul></li></ul></li>
<li><a href="/wiki/Square_Enix" title="Square Enix">Square Enix</a>
<ul><li><a href="/wiki/Visual_Works" class="mw-redirect" title="Visual Works">Visual Works</a></li></ul></li>
<li><a href="/wiki/Studio_Bind" title="Studio Bind">Studio Bind</a></li>
<li><a href="/wiki/Studio_Hibari" title="Studio Hibari">Studio Hibari</a>
<ul><li><a href="/wiki/Larx_Entertainment" title="Larx Entertainment">Larx Entertainment</a></li>
<li><a href="/wiki/Lerche_(brand)" title="Lerche (brand)">Lerche</a></li></ul></li>
<li><a href="/wiki/Tokyo_Broadcasting_System" class="mw-redirect" title="Tokyo Broadcasting System">Tokyo Broadcasting System</a>
<ul><li><a href="/wiki/Seven_Arcs" title="Seven Arcs">Seven Arcs</a></li></ul></li>
<li><a href="/wiki/Toei_Company" title="Toei Company">Toei Company</a>
<ul><li><a href="/wiki/Toei_Animation" title="Toei Animation">Toei Animation</a></li></ul></li>
<li><a href="/wiki/TV_Asahi" title="TV Asahi">TV Asahi</a>
<ul><li><a href="/wiki/Shin-Ei_Animation" title="Shin-Ei Animation">Shin-Ei Animation</a>
<ul><li><a href="/wiki/SynergySP" title="SynergySP">SynergySP</a></li></ul></li></ul></li>
<li><a href="/wiki/Twin_Engine_(company)" title="Twin Engine (company)">Twin Engine</a>
<ul><li><a href="/wiki/Geno_Studio" title="Geno Studio">Geno Studio</a></li>
<li><a href="/wiki/Lay-duce" title="Lay-duce">Lay-duce</a></li>
<li><a href="/wiki/Revoroot" title="Revoroot">Revoroot</a></li>
<li><a href="/wiki/Studio_Colorido" title="Studio Colorido">Studio Colorido</a></li></ul></li>
<li><a href="/wiki/Ultra_Super_Pictures" title="Ultra Super Pictures">Ultra Super Pictures</a>
<ul><li><a href="/wiki/Liden_Films" title="Liden Films">Liden Films</a></li>
<li><a href="/wiki/Sanzigen" title="Sanzigen">Sanzigen</a></li>
<li><a href="/wiki/Studio_Trigger" title="Studio Trigger">Trigger</a></li></ul></li>
<li><a href="/wiki/Zexcs" title="Zexcs">Zexcs</a></li></ul>
</div></td></tr></tbody></table><div></div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Inactive</th><td class="navbox-list-with-group navbox-list navbox-odd" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Artland_(company)" title="Artland (company)">Artland</a></li>
<li><a href="/wiki/Bee_Train_Production" title="Bee Train Production">Bee Train Production</a></li>
<li><a href="/wiki/Chaos_Project" title="Chaos Project">Chaos Project</a></li>
<li><a href="/wiki/Daume" title="Daume">Daume</a></li>
<li><a href="/wiki/Knack_Productions" title="Knack Productions">Knack Productions</a></li>
<li><a href="/wiki/Mook_Animation" title="Mook Animation">Mook Animation</a></li>
<li><a href="/wiki/Mushi_Production" title="Mushi Production">Mushi Production</a></li>
<li><a href="/wiki/Ordet_(studio)" title="Ordet (studio)">Ordet</a></li>
<li><a href="/wiki/Remic" title="Remic">Remic</a></li>
<li><a href="/wiki/Zuiyo" title="Zuiyo">Zuiyo</a></li></ul>
</div></td></tr><tr><th scope="row" class="navbox-group" style="width:1%">Defunct</th><td class="navbox-list-with-group navbox-list navbox-even" style="width:100%;padding:0"><div style="padding:0 0.25em">
<ul><li><a href="/wiki/Arms_(company)" title="Arms (company)">Arms</a></li>
<li><a href="/wiki/Artmic" title="Artmic">Artmic</a></li>
<li><a href="/wiki/Bandai_Visual" title="Bandai Visual">Bandai Visual</a></li>
<li><a href="/wiki/Group_TAC" title="Group TAC">Group TAC</a></li>
<li><a href="/wiki/Hal_Film_Maker" title="Hal Film Maker">Hal Film Maker</a></li>
<li><a href="/wiki/J2_Communications" title="J2 Communications">J2 Communications</a></li>
<li><a href="/wiki/Kitayama_Eiga_Seisakujo" title="Kitayama Eiga Seisakujo">Kitayama Eiga Seisakujo</a></li>
<li><a href="/wiki/Kitty_Films" title="Kitty Films">Kitty Films <small>(Mitaka Studio)</small></a></li>
<li><a href="/wiki/Kokusai_Eiga-sha" title="Kokusai Eiga-sha">Kokusai Eiga-sha</a></li>
<li><a href="/wiki/Manglobe" title="Manglobe">Manglobe</a></li>
<li><a href="/wiki/Palm_Studio" title="Palm Studio">Palm Studio</a></li>
<li><a href="/wiki/Production_IMS" title="Production IMS">Production IMS</a></li>
<li><a href="/wiki/Radix_Ace_Entertainment" title="Radix Ace Entertainment">Radix Ace Entertainment</a></li>
<li><a href="/wiki/Spectrum_Animation" title="Spectrum Animation">Spectrum Animation</a></li>
<li><a href="/wiki/Studio_Fantasia" title="Studio Fantasia">Studio Fantasia</a></li>
<li><a href="/wiki/Tear_Studio" title="Tear Studio">Tear Studio</a></li>
<li><a href="/wiki/Topcraft" title="Topcraft">Topcraft</a></li>
<li><a href="/wiki/Triangle_Staff" title="Triangle Staff">Triangle Staff</a></li>
<li><a href="/wiki/Tsuchida_Production" title="Tsuchida Production">Tsuchida Production</a></li>
<li><a href="/wiki/List_of_animation_studios_owned_by_The_Walt_Disney_Company#Disney_Animation_Japan" class="mw-redirect" title="List of animation studios owned by The Walt Disney Company">Walt Disney Animation Japan</a></li>
<li><a href="/wiki/Xebec_(studio)" title="Xebec (studio)">Xebec</a></li>
<li><a href="/wiki/Yaoyorozu" title="Yaoyorozu">Yaoyorozu</a></li></ul>'''
result = process_links(links_string)
print(result)