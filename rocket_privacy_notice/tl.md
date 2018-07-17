## <span class="privacy-header-firefox-rocket">Abiso sa Privacy ng</span> <span class="privacy-header-policy">Firefox Rocket</span>

Biernes, Mayo 11, 2018
{: datetime="2018-5-11" }

## Sa Mozilla, naniniwala kami na ang privacy ay mahalaga sa isang malusog na internet.

Iyan ang dahilan kung bakit namin binubuo ang Firefox Rocket, at lahat ng aming produkto, para makapagbigay sa iyo ng higit na kontrol sa impormasyong ibinabahagi mo online at sa impormasyong ibinabahagi mo sa amin. Hangad naming kolektahin lang kung anong kailangan namin para mapaganda ang Rocket para sa lahat.

Sa Abiso sa Privacy na ito, ipinapaliwanag namin kung anong data ang ibinabahagi ng Rocket at itinuturo sa iyo ang mga setting para magbahagi ng mas kaunti. Sumusunod din kami sa mga kasanayang nakabalangkas sa [patakaran sa privacy](https://www.mozilla.org/privacy/) ng Mozilla para sa kung paano kami tumatanggap, nangangasiwa at nagbabahagi ng impormasyong kinokolekta namin mula sa Rocket.

## Bilang default, ang Firefox Rocket ay nagbabahagi ng data para:

### Pagandahin ang performance at stability para sa mga user kahit saan

* __Data ng interaksyon__: Nagpapadala ang Rocket ng data tungkol sa iyong mga interaksyon sa Rocket sa amin (bilang ng mga webpage na binisita; at haba ng session) at mga feature ng Rocket na inaalok ng Mozilla o ng aming mga partner (gaya ng interaksyon sa mga feature ng search at referral sa search partner sa Rocket).

* __Teknikal na data__: Nagpapadala ang Rocket ng data tungkol sa iyong bersyon at wika ng Rocket; operating system at configuration ng hardware ng device; memory, pangunahing impormayon tungkol sa mga pag-crash at error; resulta ng mga naka-automate na proseso tulad ng mga update, at pag-activate sa amin. Kapag nagpapadala sa amin ng data ang Rocket, pansamantalang kinokolekta ang iyong IP address bilang bahagi ng aming mga server log.

Magbasa ng detalyadong dokumentasyon para sa Rocket [dito](https://github.com/mozilla-tw/Rocket/wiki/Telemetry) o i-off ang “Magpadala ng Data ng Paggamit” sa iyong Mga Setting.
{: #telemetry }

### Magmungkahi ng nauugnay na content

Nagpapakita ang Rocket ng content, gaya ng Mga Nangungunang Site (mga website na iminumungkahi ng Mozilla para sa mga first-time na user ng Rocket).

* __Teknikal na data at data ng Interaksyon__: Nagpapadala ang Rocket sa amin ng data gaya ng posisyon, laki at pagkakalagay ng content na iminumungkahi namin, at pati na rin ng pangunahing data tungkol sa iyong mga interaksyon sa iminumungkahing content ng Rocket. Kasama rito ang bilang ng beses na ipinapakita o kini-click ang iminumungkahing content.

### Sukatin at suportahan ang aming marketing

* __Data ng Referral at Campaign__: Para tumulong na mapaganda ang aming mga marketing campaign, maaaring gumamit ang Rocket ng “Data ng Referral” gaya ng domain ng website o advertising campaign na nag-refer sa iyo na i-download at i-install ang Rocket. Ang data na ito ay pinapanatili ng aming analytics vendor at ibinibigay kapag binuksan mo ang Rocket, at may kasama rin itong Google advertising ID, timestamp, bansa, locale, operating system, at bersyon ng app. Maaari din kaming gumamit ng mga third party na vendor para mamahala ng mga referral program at mangasiwa ng anumang data na pipiliin mong isumite.

Matuto pa tungkol sa [Data ng Referral at Campaign](https://github.com/mozilla-tw/Rocket/wiki/Telemetry#install-campaign-tracking). 

### Pagandahin ang aming produkto batay sa iyong feedback

Para tulungan kaming pagandahin ang performance, magbigay ng suporta sa mga pag-crash, unawain ang iyong karanasan sa Rocket at pagandahin ang karanasan ng user sa pamamagitan ng A/B testing at in-product na messaging, ginagamit ng Firefox Rocket ang Firebase platform ng Google, na tumatanggap ng data mula sa iyong device. Matuto pa tungkol sa pangongolekta ng data ng [Firebase](https://support.google.com/firebase/answer/6318039?hl=en) o i-off ang “Magpadala ng Data ng Paggamit” sa iyong Mga Setting. 

---

## Kung ginagamit mo ang mga feature na ito, magbabahagi ang Rocket ng data para magbigay ng functionality: {: #optional-features }

### Paghahanap

Maaari kang magsagawa ng mga paghahanap nang direkta mula sa bar ng paghahanap sa Rocket. _Hindi natatanggap ng Mozilla ang iyong mga query sa paghahanap._ Ang data ng query ay ipinapadala sa iyong search provider na may sarili nilang patakaran sa privacy.

* __Mga Suhestiyon sa Paghahanap__: Bilang default, ipinapadala ng Rocket ang mga query ng paghahanap sa iyong search provider para matulungan kang makatuklas ng mga karaniwang parirala na hinahap ng ibang mga tao at mapaganda ang iyong karanasan sa paghahanap. Hindi ipapadala ang data na ito kung hindi sinusuportahan ng napili mong search provider ang mga suhestiyon sa paghahanap.
{: #searchsuggestions }
    
### Lokasyon {: #location-services }

* __Data ng lokasyon sa geolocation service ng Google__: Palaging nagtatanong ang Rocket bago tukuyin at ibahagi ang iyong lokasyon sa isang humihiling na website (halimbawa, kung kailangan ng isang website ng mapa ang iyong lokasyon para makapagbigay ng mga direksyon). Para tukuyin ang lokasyon, maaaring gamitin ng Rocket ang mga feature ng geolocation ng iyong operating system, mga Wi-fi network, mga cell phone tower, o IP address, at maaaring ipadala ang data na ito sa geolocation service ng Google, na may sarili nilang [patakaran sa privacy](https://www.google.com/privacy/lsf.html).

[Matuto pa](https://www.mozilla.org/firefox/geolocation/).
