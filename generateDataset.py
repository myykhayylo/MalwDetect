from pathlib import Path
import pandas as pd
import featureExtraction

#quando chiamata genera un dataset con feature e lo salva nel file finalDataset.csv 
def generate(dataset,file):
    
    #create new dataset with feature
    finalDataset = pd.DataFrame(columns = ["url", 'IP', 'urlLenght',"ShortiningServ","numDash","numAt","numQM","numAmpersand","numVS","numEqual",
    "numUnderscore","numTilde","numPercente","numAsterisc","NumDollar","numSC","numColons","numSQ","dash","httpsDomSub","port","checkPath","numberSub",
    "lenghtDom","lenghtSub","lenghtPath","numLetters","numDigits","PunyCode","suspWords","https","email","TLD","label"])
        
    for i in range(len(dataset)):
        url = dataset.iloc[i]["url"]
        label = dataset.iloc[i]["status"]
        #f1 = featureExtraction.yearsFromExpiration(url)
        f2 = featureExtraction.isIP(url)
        f3 = featureExtraction.urlLenght(url)
        f4 = featureExtraction.usingShortiningServ(url)
        f5 = featureExtraction.numberOfDash(url)
        f6 = featureExtraction.numberOfAt(url)
        f7 = featureExtraction.numberOfQM(url)
        f8 = featureExtraction.numberOfAmpersand(url)
        f9 = featureExtraction.numberOfVS(url)
        f10 = featureExtraction.numberOfEqual(url)
        f11 = featureExtraction.numberOfUnderscore(url)
        f12 = featureExtraction.numberOfTilde(url)
        f13 = featureExtraction.numberOfPercente(url)
        f14 = featureExtraction.numberOfAsterisc(url)
        f15 = featureExtraction.numberOfDollar(url)
        f16 = featureExtraction.numberOfSemiColons(url)
        f17 = featureExtraction.numberOfColons(url)
        f18 = featureExtraction.numberOfSQ(url)
        f19 = featureExtraction.dashInDomOrSub(url)
        f20 = featureExtraction.httpsInDomOrSub(url)
        f21 = featureExtraction.port(url)
        f22 = featureExtraction.checkPath(url)
        f23 = featureExtraction.numberSub(url)
        f24 = featureExtraction.lenghtDom(url)
        f25 = featureExtraction.lenghtSub(url)
        f26 = featureExtraction.lenghtPath(url)
        f27 = featureExtraction.numberOfLetters(url)
        f28 = featureExtraction.numberOfDigits(url)
        f29 = featureExtraction.usingPunycode(url)
        f30 = featureExtraction.suspiciousWords(url)
        f31 = featureExtraction.checkHttps(url)
        f32 = featureExtraction.hasEmail(url)
        f33 = featureExtraction.checkTLD(url)
        
        new_row = [url,f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32,f33,label]
        finalDataset.loc[len(finalDataset)] = new_row
        
    #salva il dataset in finalDataset.csv
    finalDataset.to_csv(file,index=False)
    
    
    return finalDataset
