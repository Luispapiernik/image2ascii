# Image to ascii

Convert image to ascii easily and export to .txt or to an image format.

## Usage
The complete set of options is given by

```bash
usage: main.py [-h] [-i INPUT] [-o OUTPUT] [--format {TXT,PNG,BOTH}]
               [-ap {LONG_WITH_WHITE,LONG_WITHOUT_WHITE,SHORT_WITH_WHITE,SHORT_WITHOUT_WHITE,SHORT_DENSE_WITH_WHITE,SHORT_DENSE_WITHOUT_WHITE}] [-cp CUSTOM_PALETTE] [--invert-palette]
               [-r RATIO]
               [-f {tlwgtypo,latinmodernmonolight,dejavuserif,urwbookman,kalapi,rekha,tlwgtypewriter,latinmodernmono,dejavusansmono,ubuntumono,rachana,liberationmono,pottisreeramulu,anjalioldlipi,suravaram,notoserifcjksc,latinmodernroman,keraleeyam,garuda,nimbusmonops,notosansmono,notoserifcjktc,freesans,p052,liberationsansnarrow,kacstfarsi,padaukbook,dejavusans,nimbussans,rasa,liberationsans,nimbussansnarrow,padmaa,notoserifcjkjp,notoserifcjkhk,notoserifcjkkr,freeserif,c059,latinmodernmonocaps,latinmodernsans,uroob,yrsa,mrykacstqurn,tlwgtypist,peddana,kacstone,freemono,gayathri,notosanscjkjp,notosanscjkhk,notosanscjkkr,loma,liberationserif,padauk,kacstdigital,ubuntu,latinmodernmonoproplight,kacstpen,ponnala,notosanscjksc,laksaman,chilanka,notosanscjktc,kinnari,lohitgurmukhi,tlwgmono,latinmodernromandunhill,latinmodernsansdemicond,ramaraja,mitra,waree,sarai,manjari,umpush,latinmodernromancaps,z003,urwgothic,sawasdee,lohitbengali,kacstscreen,kacstart,saab,samyaktamil,lohitgujarati,d050000l,lohitassamese,timmana,raviprakash,latinmodernsansquotation,norasi,purisa,latinmodernmath,nimbusroman,khmeros,latinmodernmonoprop,opensymbol,gidugu,lohitdevanagari,kalimati,droidsansfallback,khmerossystem,latinmodernromanunslanted,lohittelugu,latinmodernromanslanted,ramabhadra,nats,lohitodia,karumbi,latinmodernromandemi,phetsarathot,kacstdecorative,lklug,ani,lakkireddy,lohittamilclassical,tenaliramakrishna,jamrul,pagul,lohittamil,likhan,samyakdevanagari,gurajada,notosansmonocjktc,syamalaramana,latinmodernmonolightcond,lohitmalayalam,notosansmonocjksc,notosansmonocjkkr,notosansmonocjkhk,sreekrushnadevaraya,notosansmonocjkjp,kacsttitlel,navilu,ubuntucondensed,tibetanmachineuni,kacstletter,standardsymbolsps,ori1uni,raghumalayalamsans,aakar,notomono,mukti,suranna,lohitkannada,dyuthi,meera,dhurjati,pothana2000,mandali,gubbi,mallanna,gargi,notocoloremoji,samyakgujarati,chandas,kacstbook,kacstposter,padmaabold11,sahadeva,kacstqurn,kacstnaskh,ntr,nakula,latinmodernmonoslanted,samanata,vemana2000,suruma,kacsttitle,samyakmalayalam,kacstoffice,abyssinicasil}]
               [--font-path FONT_PATH]

This program converts an image to ASCII and saves it in png and txt files

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        name of the input image
  -o OUTPUT, --output OUTPUT
                        names of the output file without format
  --format {TXT,PNG,BOTH}
                        PNG tells the program that the output is an image, TXT indicates the output is in plain text and and BOTH indicates both formats
  -ap {LONG_WITH_WHITE,LONG_WITHOUT_WHITE,SHORT_WITH_WHITE,SHORT_WITHOUT_WHITE,SHORT_DENSE_WITH_WHITE,SHORT_DENSE_WITHOUT_WHITE}, --ascii-palette {LONG_WITH_WHITE,LONG_WITHOUT_WHITE,SHORT_WITH_WHITE,SHORT_WITHOUT_WHITE,SHORT_DENSE_WITH_WHITE,SHORT_DENSE_WITHOUT_WHITE}
  -cp CUSTOM_PALETTE, --custom-palette CUSTOM_PALETTE
  --invert-palette      invert output image. Use if your display has a dark background
  -r RATIO, --ratio RATIO
  -f {tlwgtypo,latinmodernmonolight,dejavuserif,urwbookman,kalapi,rekha,tlwgtypewriter,latinmodernmono,dejavusansmono,ubuntumono,rachana,liberationmono,pottisreeramulu,anjalioldlipi,suravaram,notoserifcjksc,latinmodernroman,keraleeyam,garuda,nimbusmonops,notosansmono,notoserifcjktc,freesans,p052,liberationsansnarrow,kacstfarsi,padaukbook,dejavusans,nimbussans,rasa,liberationsans,nimbussansnarrow,padmaa,notoserifcjkjp,notoserifcjkhk,notoserifcjkkr,freeserif,c059,latinmodernmonocaps,latinmodernsans,uroob,yrsa,mrykacstqurn,tlwgtypist,peddana,kacstone,freemono,gayathri,notosanscjkjp,notosanscjkhk,notosanscjkkr,loma,liberationserif,padauk,kacstdigital,ubuntu,latinmodernmonoproplight,kacstpen,ponnala,notosanscjksc,laksaman,chilanka,notosanscjktc,kinnari,lohitgurmukhi,tlwgmono,latinmodernromandunhill,latinmodernsansdemicond,ramaraja,mitra,waree,sarai,manjari,umpush,latinmodernromancaps,z003,urwgothic,sawasdee,lohitbengali,kacstscreen,kacstart,saab,samyaktamil,lohitgujarati,d050000l,lohitassamese,timmana,raviprakash,latinmodernsansquotation,norasi,purisa,latinmodernmath,nimbusroman,khmeros,latinmodernmonoprop,opensymbol,gidugu,lohitdevanagari,kalimati,droidsansfallback,khmerossystem,latinmodernromanunslanted,lohittelugu,latinmodernromanslanted,ramabhadra,nats,lohitodia,karumbi,latinmodernromandemi,phetsarathot,kacstdecorative,lklug,ani,lakkireddy,lohittamilclassical,tenaliramakrishna,jamrul,pagul,lohittamil,likhan,samyakdevanagari,gurajada,notosansmonocjktc,syamalaramana,latinmodernmonolightcond,lohitmalayalam,notosansmonocjksc,notosansmonocjkkr,notosansmonocjkhk,sreekrushnadevaraya,notosansmonocjkjp,kacsttitlel,navilu,ubuntucondensed,tibetanmachineuni,kacstletter,standardsymbolsps,ori1uni,raghumalayalamsans,aakar,notomono,mukti,suranna,lohitkannada,dyuthi,meera,dhurjati,pothana2000,mandali,gubbi,mallanna,gargi,notocoloremoji,samyakgujarati,chandas,kacstbook,kacstposter,padmaabold11,sahadeva,kacstqurn,kacstnaskh,ntr,nakula,latinmodernmonoslanted,samanata,vemana2000,suruma,kacsttitle,samyakmalayalam,kacstoffice,abyssinicasil}, --font-name {tlwgtypo,latinmodernmonolight,dejavuserif,urwbookman,kalapi,rekha,tlwgtypewriter,latinmodernmono,dejavusansmono,ubuntumono,rachana,liberationmono,pottisreeramulu,anjalioldlipi,suravaram,notoserifcjksc,latinmodernroman,keraleeyam,garuda,nimbusmonops,notosansmono,notoserifcjktc,freesans,p052,liberationsansnarrow,kacstfarsi,padaukbook,dejavusans,nimbussans,rasa,liberationsans,nimbussansnarrow,padmaa,notoserifcjkjp,notoserifcjkhk,notoserifcjkkr,freeserif,c059,latinmodernmonocaps,latinmodernsans,uroob,yrsa,mrykacstqurn,tlwgtypist,peddana,kacstone,freemono,gayathri,notosanscjkjp,notosanscjkhk,notosanscjkkr,loma,liberationserif,padauk,kacstdigital,ubuntu,latinmodernmonoproplight,kacstpen,ponnala,notosanscjksc,laksaman,chilanka,notosanscjktc,kinnari,lohitgurmukhi,tlwgmono,latinmodernromandunhill,latinmodernsansdemicond,ramaraja,mitra,waree,sarai,manjari,umpush,latinmodernromancaps,z003,urwgothic,sawasdee,lohitbengali,kacstscreen,kacstart,saab,samyaktamil,lohitgujarati,d050000l,lohitassamese,timmana,raviprakash,latinmodernsansquotation,norasi,purisa,latinmodernmath,nimbusroman,khmeros,latinmodernmonoprop,opensymbol,gidugu,lohitdevanagari,kalimati,droidsansfallback,khmerossystem,latinmodernromanunslanted,lohittelugu,latinmodernromanslanted,ramabhadra,nats,lohitodia,karumbi,latinmodernromandemi,phetsarathot,kacstdecorative,lklug,ani,lakkireddy,lohittamilclassical,tenaliramakrishna,jamrul,pagul,lohittamil,likhan,samyakdevanagari,gurajada,notosansmonocjktc,syamalaramana,latinmodernmonolightcond,lohitmalayalam,notosansmonocjksc,notosansmonocjkkr,notosansmonocjkhk,sreekrushnadevaraya,notosansmonocjkjp,kacsttitlel,navilu,ubuntucondensed,tibetanmachineuni,kacstletter,standardsymbolsps,ori1uni,raghumalayalamsans,aakar,notomono,mukti,suranna,lohitkannada,dyuthi,meera,dhurjati,pothana2000,mandali,gubbi,mallanna,gargi,notocoloremoji,samyakgujarati,chandas,kacstbook,kacstposter,padmaabold11,sahadeva,kacstqurn,kacstnaskh,ntr,nakula,latinmodernmonoslanted,samanata,vemana2000,suruma,kacsttitle,samyakmalayalam,kacstoffice,abyssinicasil}
                        font to be used for the conversion
  --font-path FONT_PATH
```

## Some Examples

# TODO
 - Implement a method to deal with diferents methodologiest for scaling.
 - Add support for custom fonts and change the palettes according to the font,
   for this is necessary to calculate what is the density of black (or white) per
   character.
 - Add support for writing to different image's formats (png, jpg, jpeg, bmp, ...)
 - Add support for colorized images.
 - Add support for video.
