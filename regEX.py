from utils import compare_output,find_substrings
import os

def to_lowercase(strings):
    return [s.lower() for s in strings]

schema_data=dict()
schema_data["species"]=to_lowercase(['Canis lupus familiaris', 'Arabidopsis thaliana', 'Xenopus tropicalis', 'Maize', 'Drosophila melanogaster', 'Danio rerio', 'Ambystoma mexicanum', 'Gallus gallus', 'Homo sapiens', 'Rattus norvegicus', 'Mus musculus', 'Macaca fascicularis', 'Glycine max', 'Xenopus laevis', 'Caenorhabditis elegans', 'Oryctolagus cuniculus', 'Phalaenopsis aphrodite', 'Sus scrofa'])
schema_data["tissues"]=to_lowercase(['Skin', 'Brain', 'Colon', 'Eymbro', 'Cortex', 'Gastrula', 'Bone', 'Embryo', 'Ileum', 'Spinal cord', 'Gland', 'Lymph', 'Liver', 'Basal cell', 'Plant part', 'Muscle', 'Thymus', 'Cervical', 'Leaf', 'Uterus', 'Skeleton', 'Bladder', 'Spleen', 'Epithelium', 'Lacrimal Gland', 'Lung', 'Overian', 'Bone marrow', 'Stress granules', 'Kidney', 'Neuron', 'Cerebella', 'Pancreas', 'Flower', 'Cell line', 'Pituitary', 'Blood vessel', 'Stomach', 'Blastema', 'Legs', 'Intestine', 'Head Neck', 'Blood', 'Breast', 'Prostate', 'Dorsal aorta', 'Synovial', 'Eye', 'Heart', 'Mucosa', 'Ovarian', 'Tumor', 'Ear'])
schema_data["organ_parts"]=to_lowercase(['Main olfactory bulb', 'Gastric cancer', 'Detrusor layer of bladder', 'Prostate epithelial organoids', 'Upper pulmonary brances', 'Larvae', 'Tibialis anterior muscle', 'Mouse Embryo', 'Embryo', 'Main olfactory epithelium', 'Human cell lines', 'Gastrulation', 'Gonad tissue', 'MC38 syngeneic tumor', 'Cervical tissue', 'Primary PDAC tumor', 'Renal pelvis', ' Striatum', 'Coronal brain section', 'Fetal liver', 'B16F10 syngeneic tumor', 'Adrenal tissue', 'Whole Bladder', 'Transmural cross-section of the heart', 'Skin', 'hypothalamus', 'SHY neuroblasts', 'Olfactory bulb', 'Angiomyolipoma (AML)', 'GAN-KP tumor', 'Mouse aorta', 'Mouse atrium', 'Postmortem Lung', 'Embryo implantation site', 'Primary colorectal cancer', 'Mouse ventricle', 'Postmortem brain', 'Liver tissue', 'Myocardium', 'Ileum', 'Femur', 'Hindpaw', 'Nodule', 'Bartilage', 'Breast Cancer', 'Atopic dermatitis lesional skin', 'Bone', 'Leaf', 'Colorectal tissue', 'IPS cells', 'Brain', 'Right atrial appendage (RAA)', 'Glioblastoma multiforme tissue', 'GBM Tissue', 'Microglia', 'Medulla', 'Whole Mouse Bladder', 'Oral mucosa', 'Prostatic cancer', 'Heart', 'NIH3T3 cells', 'Coronal Brain', 'Dissociated Mouse Bladder', 'Lumbar spinal cord (L3/L4)', 'Gastruloid', 'SAM', 'Tail skin', 'Cauline leaf', 'Breast cancer', 'Neural tube', 'Root', 'Angiosarcomas', 'Suprachiasmatic nucleus', 'Hippocampus', 'Pancreatic adenocarcinoma', 'Trunk', 'HeLa cells', 'Muscle-invasive bladder cancer', 'Frontal cortex', 'CRLM', 'Representative psoas major muscle', 'lymphoma', 'Kidney organoid', 'Skeletal muscle (quadriceps)', 'Atopic dermatitis non-lesional skin', 'Gastrulation embryos', 'Sagittal suture', 'Visual cortex', 'Pancreatic cancer', 'Stem', 'Lung organoid', 'Follicles', 'Liver', 'Whole Bladder Nuclear', 'Squamous Cell Carcinoma', 'Basal cell carcinoma', 'ccRCC tumor', 'Coronal brain', 'Left ventricular needle (LV)', 'Colon', 'Lumbar spinal cord (L5/S1)', 'Synovial tissue', 'Sagittal section', 'Kidney-resident macrophages (KRMs)', 'Dorsolateral prefrontal cortex', 'Cervical cancer', 'Human cortex', 'Mature olfactory sensory neuron', 'Donor pancreas', 'Cortex', 'Adenoid cystic carcinoma of lacrimal gland', 'Skeletal Muscle', 'Skin irAE'])
schema_data["technologies"]=to_lowercase(['CITE-seq', 'XYZeq', 'CUT&Tag', 'RNA-seq', 'STARmap', 'DBiT-seq', 'scATAC-seq', 'scRNA', 'EASI-FISH', 'PIC-seq', 'sci-Space', 'sciMAP-ATAC-seq', 'Slide-seqV2', 'Spatial Transcriptomics', 'seqFish', 'seqFISH+', 'Stereo-Seq', '10x Visium', ' RNA-seq', 'scATAC', 'LCM-seq', 'Tomo-seq', 'Proximity RNA-seq', 'sci-ATAC-seq', 'ClampFISH', 'VINE-seq', 'snRNA', 'HDST', 'GeoMx DSP', 'Seq-Scope', 'APEX-seq', 'RNAseq', 'MERFISH', 'ClumpSeq', 'Geo-seq', 'Slide-seq'])
schema_data["disease"]=to_lowercase(['Squamous carcinoma', 'Prostate Cancer', 'Heart development', 'Lumbar spinal cord', 'Hepatocellular Carcinoma', 'Pan cancer', 'Donor pancreas', 'Cerebella development', 'Normal', 'renal cell cancer', 'Brain injury', 'Murine ischemia ', 'Breast cancer', 'Embryo development', 'Quiescent', 'Liver development', ' Recurrent ', 'Gestation development', 'Intestinal development ', 'Gynecological cancer', 'Alzheimer disease', 'Rotator cuff tear', 'Breast Cancer', 'Tissue repair', 'Atopic dermatitis', 'Psoriatic disease', 'N_HPV ', 'Acute kidney injury', 'Cutaneous Malignant Melanoma', 'Tumor metastasis', 'Muscle regeneration', 'Prostate injury', 'Prostatic cancer', 'Brain cortex', 'Lung fibrosis', 'brain metastases cancer', 'Acne', 'Head and neck angiosarcoma', 'Ductal carcinoma in situ', ' Atopic dermatitis ', '\u200cHeptablastoma cancer', 'Embryonic development', 'Lung cancer', 'Kidney injury', ' HSIL_HPV ', 'Cervical squamous cell carcinoma', 'Adenoid cystic carcinoma of the lacrimal gland', 'Cancer', 'Heart failure', 'Chronic Inflammatory Disease', 'Melanoma', 'colorectal cancer ', 'Nornal atlas', 'Hepatic ischemia-reperfusion', ' Psoriasis, Lichen planus ', 'Basal cell carcinoma', 'Wilms Tumors cancer', 'Brain Cortex Olfactory bulb ', 'Bone marrow', 'Lung cancer development', 'Lung development', 'Normal atlas', 'Brain Hippocampus', 'Intraductal Papillary Mucinous Neoplasms cancer', ' Cortex with astrogliosis ', 'Injured brain', 'Schizophrenia and Autism spectrum disorder', 'Zika virus', 'Pancreatic cancer', 'Neuron regeneration', 'Spin cord development', ' Psoriasis ', ' hippocampus with focal neuronal loss ', 'Brain Hypothalamus', 'Head and neck squamous carcinoma (HNSCC) ', 'Gland development', 'Bacterial', 'Diabetic Ischemic Limb Rescue', 'Lung Normal atlas', 'Hippocampus', 'Melanoma metastasis', ' Lichen planus ', 'Colon regeneration and repair', 'Glioblastoma', 'Hindlimb muscle regeneration', 'Brain metastases cancer', 'Dermatitis and Colitis', 'Primary ', 'Rheumatoid arthritis (RA) and Spondyloarthritis (SpA)', 'Olfactory bulb', 'Squamous cell carcinoma', 'HPV', 'Colorectal cancer', 'Epithelium injury', 'hepatoblastoma murine ', 'Pancreatic ductal adeno carcinoma', 'E9.5 Pax2GFP Mus musculus embryos', 'Myocardial Ischemia-Reperfusion Injury', 'Bladder cancer', 'T agonist', 'Infertility', 'Metastasis', 'Plants', 'Digit Regeneration', 'Primary colorectal cancer', 'Brain development', 'Skin carcinoma cancer', 'Liver injury regeneration', 'Heart regeneration and repair', 'Uninjured', 'Early Pregnancy', 'Secondary Brain Injury', 'pediatric and adult malignant gliomas', 'Psoriasis ', 'Lepromatous', ' Focal architecture abnormalities', 'Embryonic brain', 'T cell depletion', 'Cervical cancer', 'Psoriasis', 'Kidney cancer', 'Colon development', ' Pityriasis rubra pilaris ', 'Brain Cortex', 'Liver cancer', 'Paralysis', 'Angiomyolipoma', 'Neonatal heart regeneration', 'Bone Marrow', 'Endometrial Adeno carcinoma', 'Colon repair', 'Liver metastasis cancer', 'Gland repair', 'Palmitic acid ', 'wound repair', 'Primary PDAC cancer', 'Neuron', 'Invasive Ductal carcinoma', ' Reperfusion injury (IRI) and cecal ligation puncture (CLP) models of AKI', 'Skin injury', 'Gastric cancer', 'Prostate cancer', 'Pancreas development', 'Pulmonary Injury', 'CNS lymphoma', 'Heart regeneration', 'CRLM', ' Seizure epileptic brain', 'Fibrotic tendon healing', ' CA_HPV', 'Wound repair', 'Non-small cell lung cancer', 'Glioblastomas', 'Pediatric gliomas', 'Overian cancer', 'COVID-19'])
schema_data["type"]=to_lowercase(['Single-cell','Spatial transcriptomics','Single-cell and Spatial transcriptomics'])

filepath="./abstract/"
types=["species","tissues","organ_parts","technologies","disease","type"]
cnt=0
class_score=[0,0,0,0,0]
class_cnt=[0,0,0,0,0]
total_score=0
for root,dir,files in os.walk(filepath):
        for file in files:
            if cnt>=500:
                break
            if not (file.startswith("2")  or file.startswith("30")):
            # if file.startswith("2")  or file.startswith("30"):
                # print(os.path.join(root,file))
                lines=[]
                with open(os.path.join(root,file),encoding='utf-8') as f:
                    for line in f:
                        lines.append(line.strip('\n'))
                abstract=lines[5].lower()
                # abstract="brain"
                for i in range(5):
                    cnt+=1
                    lastword=find_substrings(abstract,list(schema_data[types[i]]))
                    # 查询标答并比较
                    if lastword=="ERROR":
                        errfile=open("error.txt","a+",encoding="utf-8")
                        print("ERROR in ",file,"type=",types[i])
                        print(f"-----{file}-----",file=errfile)
                        print("ERROR in ",file,"type=",types[i],file=errfile)
                        print("-----------",file=errfile)
                        errfile.close()
                    else:
                        
                        # print(f"-----{file}-----")
                        # print(f"lastword={lastword}")
                        # print(f"ans:{lines[i]}")
                        score=compare_output(lastword.lower(),lines[i].lower())
                        # if len(eval(lastword))==0:
                        #     score=0
                        #     print(f"lastword={lastword}")
                        # else:
                        #     print(f"-----{file}-----")
                        #     print(f"len={len(lastword)}")
                        #     print(f"lastword={lastword}")
                        #     print(f"ans:{lines[i]}")
                        if score=="ERROR":
                            errfile=open("error.txt","a+",encoding="utf-8")
                            print(f"-----{file}-----",file=errfile)
                            print("ERROR in ",file,"type=",types[i])
                            print("ERROR in ",file,"type=",types[i],file=errfile)
                            print(f"lastword={lastword}",file=errfile)
                            print(f"ans:{lines[i]}",file=errfile)
                            print("-----------",file=errfile)
                            errfile.close()
                            continue
                        class_cnt[i]+=1
                        class_score[i]+=score
                        total_score+=score
                        print(f"score:{score}")

                        ansfile=open("./Ans"+str(i)+".txt","a+",encoding="utf-8")
                        print(score,file=ansfile)
                        ansfile.close()
                        print("-----------")
                    # 计算平均杰卡德相似度
        print(f"total_score:{total_score}, cnt:{cnt}")  
        print(f"average:{total_score/cnt}")                  
                        
for i in range(5):
    print(f"type: {types[i]}, class_score{class_score}, class_cnt{class_cnt}")