import numpy as np
import pandas as pd
from kneed import KneeLocator
import os
import sys

#判断运行系统类型 nt-win posix-linux
system=os.name

#建立储存文件夹
G=[]
  
#建立文件夹
file_OUTPUT=os.path.exists('OUTPUT')
file_FIGURE=os.path.exists('FIGURE')
file_DATA=os.path.exists('DATA')

if file_OUTPUT == False :
   os.mkdir('OUTPUT')
   
if file_FIGURE == False :   
   os.mkdir('FIGURE')
   
if file_DATA == False :
   os.mkdir('DATA')

    
#检测input文件
file_input=os.path.exists('Parameters.input')
if file_input==False:
   print('Warning:The "Parameters.input" does not exist.')
   G.append('Warning:The "Parameters.input" does not exist.')
   filename_input_Warning1 = "Warning_input_existing.txt" 
   output_input_Warning1=open('OUTPUT/%s'%(filename_input_Warning1),'w')
   for l in range(len(G)):
       output_input_Warning1.write(str(G[l]))
       #output_input_Warning1.write("\t")#空4个字符 可以不加
       output_input_Warning1.write("\n")#\n换行
   output_input_Warning1.close()
   sys.exit(0) #终止程序
    
#从input文件导入参数
input=open('Parameters.input','r')

input1=input.readlines() #读取全部行

G.append('Input Parameters')
G.append('--------------------------------------------------')
G.append('Universal Parameters ')
G.append('--------------------------------------------------')

io=input1[0].strip('Address of Excel') #删除io
io=io.strip() #删除空格
if io !='':
   print('Address of Excel : ',io)
io_output='Address of Excel : ' + io
G.append(io_output)

sheet_name=input1[1].strip('sheet_name') 
sheet_name=sheet_name.strip() 
if sheet_name != '' :
   print('sheet_name : ',sheet_name)
sheet_name_output='sheet name : ' + sheet_name
G.append(sheet_name_output)

k=input1[2].strip('Row of Excel Table')
k=k.strip() 
if k != '' :
   print('Row of Excel Table : ',k)
k_output='Row of Excel Table : ' + k
G.append(k_output)

dz=input1[3].strip('Space Step Length [m]')
dz=dz.strip() 
if dz != '' :
   print('Space Step Length [m] : ',dz)
dz_output='Space Step Length [m] : ' + dz
G.append(dz_output)
if 'e' in dz :
    dz=dz.replace('e','*10**(')
    dz=dz + ')'
if 'E' in dz :
    dz=dz.replace('E','*10**(')
    dz=dz + ')'


Z=input1[4].strip('Space Steps')
Z=Z.strip()
if Z != '' :
   print('Space Steps : ',Z)
Z_output='Space Steps : ' + Z
G.append(Z_output)
if 'e' in Z :
    Z=Z.replace('e','*10**(')
    Z=Z + ')'
if 'E' in Z :
    Z=Z.replace('E','*10**(')
    Z=Z + ')'


dt=input1[5].strip('Time Step Length [h]')
dt=dt.strip() 
if dt != '' :
   print('Time Step Length [h] : ',dt)
dt_output='Time Step Length [h] : ' + dt
G.append(dt_output)
if 'e' in dt :
    dt=dt.replace('e','*10**(')
    dt=dt + ')'
if 'E' in dt :
    dt=dt.replace('E','*10**(')
    dt=dt + ')'


T=input1[6].strip('Time Steps')
T=T.strip() 
if T != '' :
   print('Time Steps : ',T)
T_output='Time Steps : ' + T
G.append(T_output)
if 'e' in T :
    T=T.replace('e','*10**(')
    T=T + ')'
if 'E' in T :
    T=T.replace('E','*10**(')
    T=T + ')'


vs=input1[7].strip('Interstitial Velocity [m/s]')
vs=vs.strip()
if vs != '' :
   print('Interstitial Velocity [m/s] : ',vs)
vs_output='Interstitial Velocity [m/s] : ' + vs
G.append(vs_output)
if 'e' in vs :
    vs=vs.replace('e','*10**(')
    vs=vs + ')'
if 'E' in vs :
    vs=vs.replace('E','*10**(')
    vs=vs + ')'


P=input1[8].strip('Pressure [Pa]')
P=P.strip()
if P != '' :
   print('Pressure [Pa] : ',P)
P_output='Pressure [Pa] : ' + P
G.append(P_output)
if 'e' in P :
    P=P.replace('e','*10**(')
    P=P + ')'
if 'E' in P :
    P=P.replace('E','*10**(')
    P=P + ')'

   
T0=input1[9].strip('Temperature [K]')
T0=T0.strip()
if T0 != '' :
   print('Temperature [K] : ',T0)
T0_output='Temperature [K] : ' + T0
G.append(T0_output)
if 'e' in T0 :
    T0=T0.replace('e','*10**(')
    T0=T0 + ')'
if 'E' in T0 :
    T0=T0.replace('E','*10**(')
    T0=T0 + ')'


eb=input1[10].strip('Porosity of the Bed')
eb=eb.strip()
if eb != '' :
   print('Porosity of the Bed : ',eb)
eb_output='Porosity of the Bed : ' + eb
G.append(eb_output)
if 'e' in eb :
    eb=eb.replace('e','*10**(')
    eb=eb + ')'
if 'E' in eb :
    eb=eb.replace('E','*10**(')
    eb=eb + ')'


ep=input1[11].strip('Porosity of the Adsorbent Particles')
ep=ep.strip()
if ep != '' :
   print('Porosity of the Adsorbent Particles : ',ep)
ep_output='Porosity of the Adsorbent Particles : ' + ep
G.append(ep_output)
if 'e' in ep :
    ep=ep.replace('e','*10**(')
    ep=ep + ')'
if 'E' in ep :
    ep=ep.replace('E','*10**(')
    ep=ep + ')'


BTTC=input1[12].strip('Breakthrough Time Calculation')
BTTC=BTTC.strip()
if BTTC != '' :
   print('Breakthrough time calculation :',BTTC)
BTTC_output='Breakthrough Time Calculation : ' + BTTC
G.append(BTTC_output)


A_name=input1[14].strip('Component A')
A_name=A_name.strip()
if A_name == '' :
   A_name = 'A'

yA=input1[15].strip('molar fraction')
yA=yA.strip()
if yA != 0 and yA != '':
   print('Component A :', A_name) 
   print('molar fraction for A : ',yA) 
   G.append(' ') 
   A_name_output='Component A : '+ A_name
   G.append(A_name_output)
   yA_output='molar fraction : ' + yA
   G.append(yA_output)
#转换为可计算   
if 'e' in yA :
    yA=yA.replace('e','*10**(')
    yA=yA + ')'
if 'E' in yA :
    yA=yA.replace('E','*10**(')
    yA=yA + ')'
if yA == '' : #不输入则为0
   yA = str(0)

DLAS=input1[16].strip('axial dispersion cofficient [m^2/s]')
DLAS=DLAS.strip()
if DLAS != '' :
   print('axial dispersion cofficient for A [m^2/s] : ',DLAS)
if DLAS != 0 and DLAS != '':
   DLAS_output='axial dispersion cofficient [m^2/s] : ' + DLAS
   G.append(DLAS_output)
#转换为可计算
if 'e' in DLAS :
    DLAS=DLAS.replace('e','*10**(')
    DLAS=DLAS + ')'
if 'E' in DLAS :
    DLAS=DLAS.replace('E','*10**(')
    DLAS=DLAS + ')'
if DLAS == '':
   DLAS = str(0)


B_name=input1[18].strip('Component B')
B_name=B_name.strip()
if B_name == '' :
   B_name = 'B'

yB=input1[19].strip('molar fraction')
yB=yB.strip()   
if yB != 0 and yB != '':
   print('Component B :', B_name)
   print('molar fraction for B : ',yB) 
   G.append(' ') 
   B_name_output='Component B : '+ B_name
   G.append(B_name_output)
   yB_output='molar fraction : ' + yB
   G.append(yB_output)
#转换为可计算   
if 'e' in yB :
    yB=yB.replace('e','*10**(')
    yB=yB + ')'
if 'E' in yB :
    yB=yB.replace('E','*10**(')
    yB=yB + ')'
if yB == '' : #不输入则为0
   yB = str(0)

DLBS=input1[20].strip('axial dispersion cofficient [m^2/s]')
DLBS=DLBS.strip()
if DLBS != '' :
   print('axial dispersion cofficient for B [m^2/s] : ',DLBS)
if DLBS != 0 and DLBS != '':
   DLBS_output='axial dispersion cofficient [m^2/s] : ' + DLBS
   G.append(DLBS_output)
#转换为可计算
if 'e' in DLBS :
    DLBS=DLBS.replace('e','*10**(')
    DLBS=DLBS + ')'
if 'E' in DLBS :
    DLBS=DLBS.replace('E','*10**(')
    DLBS=DLBS + ')'
if DLBS == '':
   DLBS = str(0)


C_name=input1[22].strip('Component C')
C_name=C_name.strip()
if C_name == '' :
   C_name = 'C'

yC=input1[23].strip('molar fraction')
yC=yC.strip()
if yC != 0 and yC != '':
   print('Component C :', C_name) 
   print('molar fraction for C : ',yC) 
   G.append(' ') 
   C_name_output='Component C : '+ C_name
   G.append(C_name_output)
   yC_output='molar fraction : ' + yC
   G.append(yC_output)
#转换为可计算   
if 'e' in yC :
    yC=yC.replace('e','*10**(')
    yC=yC + ')'
if 'E' in yC :
    yC=yC.replace('E','*10**(')
    yC=yC + ')'
if yC == '' : #不输入则为0
   yC = str(0)

DLCS=input1[24].strip('axial dispersion cofficient [m^2/s]')
DLCS=DLCS.strip()
if DLCS != '' :
   print('axial dispersion cofficient for C [m^2/s] : ',DLCS)
if DLCS != 0 and DLCS != '':
   DLCS_output='axial dispersion cofficient [m^2/s] : ' + DLCS
   G.append(DLCS_output)
#转换为可计算
if 'e' in DLCS :
    DLCS=DLCS.replace('e','*10**(')
    DLCS=DLCS + ')'
if 'E' in DLCS :
    DLCS=DLCS.replace('E','*10**(')
    DLCS=DLCS + ')'
if DLCS == '':
   DLCS = str(0)


D_name=input1[26].strip('Component D')
D_name=D_name.strip()
if D_name == '' :
   D_name = 'D'

yD=input1[27].strip('molar fraction')
yD=yD.strip()
if yD != 0 and yD != '':
   print('Component D :', D_name) 
   print('molar fraction for D : ',yD) 
   G.append(' ') 
   D_name_output='Component D : '+ D_name
   G.append(D_name_output)
   yD_output='molar fraction : ' + yD
   G.append(yD_output)
#转换为可计算   
if 'e' in yD :
    yD=yD.replace('e','*10**(')
    yD=yD + ')'
if 'E' in yD :
    yD=yD.replace('E','*10**(')
    yD=yD + ')'
if yD == '' : #不输入则为0
   yD = str(0)

DLDS=input1[28].strip('axial dispersion cofficient [m^2/s]')
DLDS=DLDS.strip()
if DLDS != '' :
   print('axial dispersion cofficient for D [m^2/s] : ',DLDS)
if DLDS != 0 and DLDS != '':
   DLDS_output='axial dispersion cofficient [m^2/s] : ' + DLDS
   G.append(DLDS_output)
#转换为可计算
if 'e' in DLDS :
    DLDS=DLDS.replace('e','*10**(')
    DLDS=DLDS + ')'
if 'E' in DLDS :
    DLDS=DLDS.replace('E','*10**(')
    DLDS=DLDS + ')'
if DLDS == '':
   DLDS = str(0)

G.append(' ')   

input.close

G.append('Parameters for Adsorbate')
G.append('--------------------------------------------------')

#检查input文件是否存在所有参数
y=yA+yB+yC+yD
DL=DLAS+DLBS+DLCS+DLDS
if io=='' or sheet_name=='' or k=='' or dz=='' or Z=='' or dt=='' or T=='' or vs=='' or P=='' or T0=='' or eb=='' or ep=='' or BTTC=='' or y==0 or DL==0 :
   print('Warning:Invalid parameters, please check.')
   G.append('Warning:Invalid parameters, please check.')
   filename_input_Warning2 = "Warning_input_parameters.txt" 
   output_input_Warning2=open('OUTPUT/%s'%(filename_input_Warning2),'w')
   for l in range(len(G)):
       output_input_Warning2.write(str(G[l]))
       #output_input_Warning2.write("\t")#空4个字符 可以不加
       output_input_Warning2.write("\n")#\n换行
   output_input_Warning2.close()
   sys.exit() #终止程序
   
#固定系数 
#时间单位：h 空间单位：m
dz=eval(dz) #空间步长 eval()转换文字为运算 使用float()无法输入科学计数法的内容
Z=int(eval(Z)) #空间步数 #固定床长L=dz*Z
L=dz*Z
dt=eval(dt) #时间步长 时间t=T*dt
T=int(eval(T))#初始时间步数
vs=eval(vs) 
v=vs*3600 #间隙速度0.0023m/S 
eb=eval(eb) #床层孔隙率
ep=eval(ep) #颗粒孔隙率
E=(1-eb)/eb


#总压 温度
P=eval(P)
R=8.314
T0=eval(T0) #298K


#各组分摩尔分数
yA=eval(yA)
yB=eval(yB)
yC=eval(yC)
yD=eval(yD)


#进料浓度
CA_0=yA*P/(R*T0)
CB_0=yB*P/(R*T0)
CC_0=yC*P/(R*T0)
CD_0=yD*P/(R*T0)


#加速识别阈值（10%C0）
CA_10=0.1*CA_0
CB_10=0.1*CB_0
CC_10=0.1*CC_0
CD_10=0.1*CD_0


#A-C2H2, B-C2H4, C-C2H6, D-CO2
DLAS=eval(DLAS)
DLBS=eval(DLBS)
DLCS=eval(DLCS)
DLDS=eval(DLDS)

DLA=DLAS*3600
DLB=DLBS*3600
DLC=DLCS*3600
DLD=DLDS*3600


#导入数据
#第二行为0行
k=int(k)

table = pd.read_excel(io,sheet_name=int(sheet_name))#表格从0算起

#编号或名字
No_or_Name=table.iloc[k,0]#先转换为字符串才可以判断是否为数字
Nonan=np.isnan(No_or_Name)
if Nonan==True:
   No_or_Name='adsorbate'
print('No or Name : ',No_or_Name)      
#判断输入的是编号还是名字
No_or_Name=str(No_or_Name)
No=No_or_Name.isnumeric()
if No=='True':
   No_or_Name=int(No_or_Name)
No_or_Name_output='Adsorbate : '+No_or_Name
G.append(No_or_Name_output)
  
#材料及气体参数
Pc=table.iloc[k,1]#材料的密度
Pcnan=np.isnan(Pc)
if Pcnan == False:
   print('Density of adsorbate [kg/m^3] : ',Pc)  
   Pc_output='Density of adsorbate [kg/m^3] : '+str(Pc)
   G.append(Pc_output)
   
Pb=Pc*(1-eb)*(1-ep)#床层密度
Pbnan=np.isnan(Pb)
if Pbnan == False:
   print('Density of bed [kg/m^3] : ',Pb) 
   Pb_output='Density of bed [kg/m^3] : '+str(Pb)
   G.append(Pb_output)
  
Ps=Pc*(1-ep)#颗粒密度
Psnan=np.isnan(Ps)
if Psnan == False:
   print('Density of particle [kg/m^3] : ',Ps)
   Ps_output='Density of particle [kg/m^3] : '+str(Ps)
   G.append(Ps_output)
    
#饱和吸附量
G.append('Saturation value of adsorbate loading [mol/kg]')

qmA=table.iloc[k,2]
qmAnan=np.isnan(qmA)
if qmAnan == False and qmA != 0 and yA != 0:
   print('Saturation value of adsorbate loading for A [mol/kg] : ', qmA) 
   qmA_output='A : '+str(qmA)
   G.append(qmA_output)
if qmAnan==True:
   qmA=0
   
qmB=table.iloc[k,3]
qmBnan=np.isnan(qmB)
if qmBnan == False and qmB != 0 and yB != 0:
   print('Saturation value of adsorbate loading for B [mol/kg] : ', qmB) 
   qmB_output='B : '+str(qmB)
   G.append(qmB_output)
if qmBnan==True:
   qmB=0
   
qmC=table.iloc[k,4]
qmCnan=np.isnan(qmC)
if qmCnan == False and qmC != 0 and yC != 0:
   print('Saturation value of adsorbate loading for C [mol/kg] : ', qmC) 
   qmC_output='C : '+str(qmC)
   G.append(qmC_output)
if qmCnan==True:
   qmC=0
   
qmD=table.iloc[k,5]
qmDnan=np.isnan(qmD)
if qmDnan == False and qmD != 0 and yD != 0:
   print('Saturation value of adsorbate loading for D [mol/kg] : ', qmD) 
   qmD_output='D : '+str(qmD)
   G.append(qmD_output)
if qmDnan==True:
   qmD=0
    
#朗缪尔系数
G.append('Equilibrium constant of Langmuir [m^3/mol]')

bA=table.iloc[k,6]
bAnan=np.isnan(bA)
if bAnan == False and bA != 0 and yA != 0:
   print('Equilibrium constant of Langmuir for A [m^3/mol] : ', bA)  
   bA_output='A : '+str(bA)
   G.append(bA_output)
if bAnan==True:
   bA=0
 
bB=table.iloc[k,7]
bBnan=np.isnan(bB)
if bBnan == False and bB != 0 and yB != 0:
   print('Equilibrium constant of Langmuir for B [m^3/mol] : ', bB) 
   bB_output='B : '+str(bB)
   G.append(bB_output)
if bBnan==True:
   bB=0
   
bC=table.iloc[k,8]
bCnan=np.isnan(bC)
if bCnan == False and bC != 0 and yC != 0:
   print('Equilibrium constant of Langmuir for C [m^3/mol] : ', bC)
   bC_output='C : '+str(bC)
   G.append(bC_output)
if bCnan==True:
   bC=0
   
bD=table.iloc[k,9]
bDnan=np.isnan(bD)
if bDnan == False and bD != 0 and yD != 0:
   print('Equilibrium constant of Langmuir for D [m^3/mol] : ', bD) 
   bD_output='D : '+str(bD)
   G.append(bD_output)
if bDnan==True:
   bD=0

#传质系数
G.append('Overall mass transfer coefficient [s-1]')
if bA == 0 :
   KAs=0
if bA != 0 :
   KAs=table.iloc[k,10]
KAsnan=np.isnan(KAs)
if KAsnan==False and KAs != 0 and yA != 0:
   print('Overall mass transfer coefficient for A [s-1] : ', KAs)
   KAs_output='A : '+str(KAs)
   G.append(KAs_output)
if KAsnan==True:
   KAs=0
       
if bB == 0 :
   KBs=0
if bB != 0 :
   KBs=table.iloc[k,11]
KBsnan=np.isnan(KBs)
if KBsnan==False and KBs != 0 and yB != 0:
   print('Overall mass transfer coefficient for B [s-1] : ', KBs)
   KBs_output='B : '+str(KBs)
   G.append(KBs_output)
if KBsnan==True:
   KBs=0
       
if bC == 0 :
   KCs=0
if bC != 0 :
   KCs=table.iloc[k,12]
KCsnan=np.isnan(KCs)
if KCsnan==False and KCs != 0 and yC != 0:
   print('Overall mass transfer coefficient for C [s-1] : ', KCs)
   KCs_output='C : '+str(KCs)
   G.append(KCs_output)
if KCsnan==True:
   KCs=0
       
if bD == 0 :
   KDs=0
if bD != 0 :
   KDs=table.iloc[k,13]
KDsnan=np.isnan(KDs)
if KDsnan==False and KDs != 0 and yD != 0:
   print('Overall mass transfer coefficient for D [s-1] : ', KDs)
   KDs_output='D : '+str(KDs)
   G.append(KDs_output)
if KDsnan==True:
   KDs=0

G.append('')
G.append('Simulated Finish')
G.append('--------------------------------------------------')
G.append('')

#检查EXCEL
qmA_D=qmA+qmB+qmC+qmD
bA_D=bA+bB+bC+bD
KA_Ds=KAs+KBs+KCs+KDs
if  Pcnan==True or Pbnan==True or Psnan==True or qmA_D==0 or bA_D==0 or KA_Ds==0 :
   print('Warning:Invalid parameters in excel table, please check.')
   G.append('Warning:Invalid parameters in excel table, please check.')
   filename_input_Warning3 = "Warning_excel_parameters.txt" 
   output_input_Warning3=open('OUTPUT/%s'%(filename_input_Warning3),'w')
   for l in range(len(G)):
       output_input_Warning3.write(str(G[l]))
       #output_input_Warning3.write("\t")#空4个字符 可以不加
       output_input_Warning3.write("\n")#\n换行
   output_input_Warning3.close()
   sys.exit() #终止程序

     
#换单位
KA=KAs*3600
KB=KBs*3600
KC=KCs*3600
KD=KDs*3600
      
    
#建立网格
A=np.zeros([Z+1,T+1])
B=np.zeros([Z+1,T+1])
C=np.zeros([Z+1,T+1])
D=np.zeros([Z+1,T+1])

qA=np.zeros([Z+1,T+1])
qB=np.zeros([Z+1,T+1])
qC=np.zeros([Z+1,T+1])
qD=np.zeros([Z+1,T+1])
    

t=T*dt   
space_time=np.arange(0,(T+1)*dt,dt)#不包括最后一个数
max_time=np.max(space_time)
if max_time>t:
   space_time=space_time[0:T+1] #去除由于python的BUG多出的数

#收敛检测
cmax=P/(R*T0)
#print(cmax)

#边界条件
for j in np.arange(1,T+1):
    A[0,j]=CA_0
    B[0,j]=CB_0
    C[0,j]=CC_0
    D[0,j]=CD_0
    qA[Z,j]=0
    qB[Z,j]=0
    qC[Z,j]=0
    qD[Z,j]=0
   
#初始条件
for i in np.arange(0,Z+1):
    A[i,0]=0
    B[i,0]=0
    C[i,0]=0
    D[i,0]=0
    qA[i,0]=0
    qB[i,0]=0
    qC[i,0]=0
    qD[i,0]=0
    
        
#递推关系
for j in np.arange(0,T):
    for i in np.arange(1,Z):
  #吸附量
#A     
        if yA != 0:             
           A[i,j+1]=dt*(((DLA/(dz**2))+v/dz)*A[i-1,j]+(1/dt-v/dz-(2*DLA)/(dz**2))*A[i,j]+(DLA/(dz**2))*A[i+1,j]
                            -(Ps*E*KA*(((bA*qmA*A[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qA[i,j])))
           
           qA[i,j+1]=KA*dt*(((bA*qmA*A[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qA[i,j])+qA[i,j]
           
        
      
#B      
        if yB != 0:      
           B[i,j+1]=dt*(((DLB/(dz**2))+v/dz)*B[i-1,j]+(1/dt-v/dz-(2*DLB)/(dz**2))*B[i,j]+(DLB/(dz**2))*B[i+1,j]
                            -(Ps*E*KB*(((bB*qmB*B[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qB[i,j])))
           
           qB[i,j+1]=KB*dt*(((bB*qmB*B[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qB[i,j])+qB[i,j]
           
        
           
#C     
        if yC != 0:           
           C[i,j+1]=dt*(((DLC/(dz**2))+v/dz)*C[i-1,j]+(1/dt-v/dz-(2*DLC)/(dz**2))*C[i,j]+(DLC/(dz**2))*C[i+1,j]
                            -(Ps*E*KC*(((bC*qmC*C[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qC[i,j])))
           
           qC[i,j+1]=KC*dt*(((bC*qmC*C[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qC[i,j])+qC[i,j]
           
        
           
#D     
        if yD != 0:                       
           D[i,j+1]=dt*(((DLD/(dz**2))+v/dz)*D[i-1,j]+(1/dt-v/dz-(2*DLD)/(dz**2))*D[i,j]+(DLD/(dz**2))*D[i+1,j]
                            -(Ps*E*KD*(((bD*qmD*D[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qD[i,j])))
           
           qD[i,j+1]=KD*dt*(((bD*qmD*D[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qD[i,j])+qD[i,j]
           
#自测不收敛提前中止  
        nanA=np.isnan(A[i,j+1])
        nanB=np.isnan(B[i,j+1])
        nanC=np.isnan(C[i,j+1])
        nanD=np.isnan(D[i,j+1])
        if A[i,j+1] > cmax or B[i,j+1] > cmax or C[i,j+1] > cmax or D[i,j+1] > cmax or nanA ==True or nanB ==True or nanC ==True or nanD ==True or qA[i,j+1] < 0 or qB[i,j+1] < 0 or qC[i,j+1] < 0 or qD[i,j+1] < 0:
           break 
                        
    for i in np.arange(Z,Z+1):
        if yA != 0:
           A[i,j+1]=A[i-1,j+1]
           
        if yB != 0:
           B[i,j+1]=B[i-1,j+1]
           
        if yC != 0:
           C[i,j+1]=C[i-1,j+1]
           
        if yD != 0:   
            D[i,j+1]=D[i-1,j+1]

#自测不收敛提前中止
        nanA=np.isnan(A[i,j+1])
        nanB=np.isnan(B[i,j+1])
        nanC=np.isnan(C[i,j+1])
        nanD=np.isnan(D[i,j+1])
        if A[i,j+1] > cmax or B[i,j+1] > cmax or C[i,j+1] > cmax or D[i,j+1] > cmax or nanA ==True or nanB ==True or nanC ==True or nanD ==True :
           break         
print('The calculation of breakthrough curve has been finished')

#检查       
A_min=np.min(A)
A_max=np.max(A)
qA_min=np.min(qA)
nanA_max=np.isnan(A_max)#nan判定
nanA_min=np.isnan(A_min)
nanqA_min=np.isnan(qA_min)
    
B_min=np.min(B)
B_max=np.max(B)
qB_min=np.min(qB)
nanB_max=np.isnan(B_max)
nanB_min=np.isnan(B_min)
nanqB_min=np.isnan(qB_min)
    
C_min=np.min(C)
C_max=np.max(C)
qC_min=np.min(qC)
nanC_max=np.isnan(C_max)
nanC_min=np.isnan(C_min)
nanqC_min=np.isnan(qC_min)
    
D_min=np.min(D)
D_max=np.max(D)
qD_min=np.min(qD)
nanD_max=np.isnan(D_max)
nanD_min=np.isnan(D_min)
nanqD_min=np.isnan(qD_min)


#是否计算穿透时间  
if BTTC=='Yes' :   
   if A_min<0  or qA_min<0 or A_max>cmax or B_min<0 or qB_min<0 or B_max>cmax or C_min<0  or qC_min<0 or C_max>cmax or  D_min<0  or qD_min<0 or D_max>cmax or nanA_max==True or nanA_min==True or nanqA_min==True or nanB_max==True or nanB_min==True or nanqB_min==True or nanC_max==True or nanC_min==True or nanqC_min==True or nanD_max==True or nanD_min==True or nanqD_min==True:
      print('Warning : It was not converge. Please try to set smaller Time Step Length & Space Step Length.')
                        
   if A_min==0 and  qA_min==0 and A_max<=cmax and B_min==0 and  qB_min==0 and B_max<=cmax and C_min==0 and  qC_min==0 and C_max<=cmax and D_min==0 and qD_min==0 and D_max<=cmax :
#计算突破时间
      if yA !=0 :
         for tA in np.arange(0,T+1):
             C_A = A[Z,tA]
             dC_A = C_A - CA_10
             if dC_A >= 0 :
                t_A = tA
                #print(t_A)
                break #中止运行循环 continue表示跳过条件，继续运行
             if tA==T and dC_A<0 :
                print('Warning : please set larger Time Steps')
             
      if yA ==0 :
         t_A=0
         dC_A=0
       
       
      if yB !=0 :
         for tB in np.arange(0,T+1):
             C_B = B[Z,tB]
             dC_B = C_B - CB_10
             if dC_B >= 0 :
                t_B = tB
                #print(t_B)
                break #中止运行循环 continue表示跳过条件，继续运行
             if tB==T and dC_B<0 :
                print('Warning : please set larger Time Steps')
             
      if yB ==0 :
         t_B=0 
         dC_B=0

              
      if yC !=0 :
         for tC in np.arange(0,T+1):
             C_C = C[Z,tC]
             dC_C = C_C - CC_10
             if dC_C >= 0 :
                t_C = tC
                #print(t_C)
                break #中止运行循环 continue表示跳过条件，继续运行
             if tC==T and dC_C<0 :
                print('Warning : please set larger Time Steps')
             
      if yC ==0 :
         t_C=0
         dC_C=0

              
      if yD !=0 :
         for tD in np.arange(0,T+1):
             C_D = D[Z,tD]
             dC_D = C_D - CD_10
             if dC_D >= 0 :
                t_D = tD
                #print(t_D)
                break #中止运行循环 continue表示跳过条件，继续运行
             if tD==T and dC_D<0 :
                print('Warning : please set larger Time Steps')
             
      if yD ==0 :
         t_D=0 
         dC_D=0      
       
      if dC_A<0 or dC_B<0 or dC_C<0 or dC_D<0 :              
         print('Warning: The setting time is not long enough. Please set larger Time Steps for enough time')
                     
      if dC_A>=0 and dC_B>=0 and dC_C>=0 and dC_D>=0 :                 
         if yA !=0 :
            x_A=space_time[0:t_A]
            y_A=A[Z,0:t_A]
            KNEE_A=KneeLocator(x_A,y_A,curve='convex',direction='increasing',online=False)
            print('T_A =',KNEE_A.elbow,'h')
         
         if yB !=0 : 
            x_B=space_time[0:t_B] 
            y_B=B[Z,0:t_B] 
            KNEE_B=KneeLocator(x_B,y_B,curve='convex',direction='increasing',online=False)
            print('T_B =',KNEE_B.elbow,'h')
         
         if yC !=0 :  
            x_C=space_time[0:t_C] 
            y_C=C[Z,0:t_C] 
            KNEE_C=KneeLocator(x_C,y_C,curve='convex',direction='increasing',online=False)
            print('T_C =',KNEE_C.elbow,'h')      
      
         if yD !=0 :  
            x_D=space_time[0:t_D] 
            y_D=D[Z,0:t_D] 
            KNEE_D=KneeLocator(x_D,y_D,curve='convex',direction='increasing',online=False)
            print('T_D =',KNEE_D.elbow,'h')
      
         print('Calculation Finish')


def Breakthrough_times_output():
    
    if BTTC=='No' :
       print('Warning:This is the setting for breakthrough curves calculation without the calculation of breakthrough times.')
       Material_output='Material : ' + str(No_or_Name)
       if Material_output not in G:   
          G.append(Material_output)#OUTPUT编号

       if "Warning:This is the setting for breakthrough curves calculation without the calculation of breakthrough times." not in G:
          G.append('Warning:This is the setting for breakthrough curves calculation without the calculation of breakthrough times.')        
       
       if A_min<0  or qA_min<0 or A_max>cmax or B_min<0 or qB_min<0 or B_max>cmax or C_min<0  or qC_min<0 or C_max>cmax or  D_min<0  or qD_min<0 or D_max>cmax or nanA_max==True or nanA_min==True or nanqA_min==True or nanB_max==True or nanB_min==True or nanqB_min==True or nanC_max==True or nanC_min==True or nanqC_min==True or nanD_max==True or nanD_min==True or nanqD_min==True:
          print('Warning : It was not converge. Please try to set smaller Time Step Length or Space Step Length.')
          if "Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length." not in G:
             G.append('Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length.')
             
       filename_time_error1 = "OUTPUT_" + str(No_or_Name) + ".txt"
       output_time_error1=open('OUTPUT/%s'%(filename_time_error1),'w')#带有变量，字符中带有变量，‘%s'%(变量)
       for l in range(len(G)):
           output_time_error1.write(str(G[l]))
           #output_time_error1.write("\t")
           output_time_error1.write("\n")
       output_time_error1.close()

       print('The results have been output')
    
    if BTTC=='Yes' :
        
       print("Begin to ouput results")
       
       if A_min<0  or qA_min<0 or A_max>cmax or B_min<0 or qB_min<0 or B_max>cmax or C_min<0  or qC_min<0 or C_max>cmax or  D_min<0  or qD_min<0 or D_max>cmax or nanA_max==True or nanA_min==True or nanqA_min==True or nanB_max==True or nanB_min==True or nanqB_min==True or nanC_max==True or nanC_min==True or nanqC_min==True or nanD_max==True or nanD_min==True or nanqD_min==True:
          print('Warning : It was not converge. Please try to set smaller Time Step Length or Space Step Length.')
          Material_output='Material : ' + str(No_or_Name)
          if Material_output not in G:   
             G.append(Material_output)#OUTPUT编号

#OUTPUT编号
          if "Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length." not in G:
             G.append('Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length.')        
             
          filename_time_error2 = "OUTPUT_" + str(No_or_Name) + ".txt"
          output_time_error2=open('OUTPUT/%s'%(filename_time_error2),'w')#带有变量，字符中带有变量，‘%s'%(变量)
          for l in range(len(G)):
              output_time_error2.write(str(G[l]))
              #output_time_error2.write("\t")
              output_time_error2.write("\n")
          output_time_error2.close()

          print('The results have been output')
             
                
       if A_min==0 and  qA_min==0 and A_max<=cmax and B_min==0 and  qB_min==0 and B_max<=cmax and C_min==0 and  qC_min==0 and C_max<=cmax and D_min==0 and qD_min==0 and D_max<=cmax :
          
          if dC_A<0 or dC_B<0 or dC_C<0 or dC_D<0 :
                 
             print('Warning: The setting time is not long enough. Please set larger Time Steps for enough time.')
             Material_output='Material : ' + str(No_or_Name)
             if Material_output not in G:   
                G.append(Material_output)#OUTPUT编号
#OUTPUT编号
             if "Warning: The setting time is not long enough. Please set larger Time Steps for enough time." not in G:
                G.append('Warning: The setting time is not long enough. Please set larger Time Steps for enough time.')
             filename_time_error3 = "OUTPUT_" + str(No_or_Name) + ".txt"
             output_time_error3=open('OUTPUT/%s'%(filename_time_error3),'w')#带有变量，字符中带有变量，‘%s'%(变量)
             for l in range(len(G)):
                 output_time_error3.write(str(G[l]))
                 #output_time_error3.write("\t")
                 output_time_error3.write("\n")
             output_time_error3.close()
              
          if dC_A>=0 and dC_B>=0 and dC_C>=0 and dC_D>=0 :          
#导出结果
             Material_output='Material : ' + str(No_or_Name)
             if Material_output not in G:   
                G.append(Material_output)#OUTPUT编号
#OUTPUT编号
#导出突破时间             
             if yA !=0 :
                Component_A_OUTPUT='Component A : ' + A_name
                T_A_output_h = 'Breakthrough Time [h] : ' + str(KNEE_A.elbow)
                T_A_output_min = '                [min] : ' + str(KNEE_A.elbow*60)
                T_A_output_s = '                  [s] : ' + str(KNEE_A.elbow*3600)
                C_A_C_A0_output = 'C/C0 for Breakthrough Time : ' + str(KNEE_A.elbow_y/CA_0)
                if Component_A_OUTPUT not in G :
                   G.append(Component_A_OUTPUT)
                if T_A_output_h and T_A_output_min and T_A_output_s not in G :
                   G.append(T_A_output_h)
                   G.append(T_A_output_min)
                   G.append(T_A_output_s)
                if C_A_C_A0_output not in G:
                   G.append('')  
                   G.append(C_A_C_A0_output)
               
             if yB !=0 :
                Component_B_OUTPUT='Component B : ' + B_name
                T_B_output_h = 'Breakthrough Time [h] : ' + str(KNEE_B.elbow)
                T_B_output_min = '                [min] : ' + str(KNEE_B.elbow*60)
                T_B_output_s = '                  [s] : ' + str(KNEE_B.elbow*3600)
                C_B_C_B0_output = 'C/C0 for Breakthrough Time : ' + str(KNEE_B.elbow_y/CB_0)
                if Component_B_OUTPUT not in G :
                   G.append(Component_B_OUTPUT)
                if T_B_output_h and T_B_output_min and T_B_output_s not in G :
                   G.append(T_B_output_h)
                   G.append(T_B_output_min)
                   G.append(T_B_output_s)
                if C_B_C_B0_output not in G:
                   G.append('') 
                   G.append(C_B_C_B0_output)
                   
             if yC !=0 :
                Component_C_OUTPUT='Component C : ' + C_name
                T_C_output_h = 'Breakthrough Time [h] : ' + str(KNEE_C.elbow)
                T_C_output_min = '                [min] : ' + str(KNEE_C.elbow*60)
                T_C_output_s = '                  [s] : ' + str(KNEE_C.elbow*3600)
                C_C_C_C0_output = 'C/C0 for Breakthrough Time : ' + str(KNEE_C.elbow_y/CC_0)
                if Component_C_OUTPUT not in G :
                   G.append(Component_C_OUTPUT)
                if T_C_output_h and T_C_output_min and T_C_output_s not in G :
                   G.append(T_C_output_h)
                   G.append(T_C_output_min)
                   G.append(T_C_output_s)
                if C_C_C_C0_output not in G:
                   G.append('') 
                   G.append(C_C_C_C0_output)
                   
             if yD !=0 :
                Component_D_OUTPUT='Component D : ' + D_name
                T_D_output_h = 'Breakthrough Time [h] : ' + str(KNEE_D.elbow)
                T_D_output_min = '                [min] : ' + str(KNEE_D.elbow*60)
                T_D_output_s = '                  [s] : ' + str(KNEE_D.elbow*3600)
                C_D_C_D0_output = 'C/C0 for Breakthrough Time : ' + str(KNEE_D.elbow_y/CD_0)
                if Component_D_OUTPUT not in G :
                   G.append(Component_D_OUTPUT)
                if T_D_output_h and T_D_output_min and T_D_output_s not in G :
                   G.append(T_D_output_h)
                   G.append(T_D_output_min)
                   G.append(T_D_output_s)
                if C_D_C_D0_output not in G:
                   G.append('') 
                   G.append(C_D_C_D0_output)      
                 
                   
             filename_time_output = "OUTPUT_" + str(No_or_Name) + ".txt"
             output_time_output=open('OUTPUT/%s'%(filename_time_output),'w')#带有变量，字符中带有变量，‘%s'%(变量)
             for l in range(len(G)):
                 output_time_output.write(str(G[l]))
                 #output_time_output.write("\t")
                 output_time_output.write("\n")
             output_time_output.close()

       return print('Finish')

if __name__ == "__main__" :
   Breakthrough_times_output() #import时不会被启用

def DATA_output(unit_of_time='h'):
    
    print('Begin to ouput data')
    if A_min<0  or qA_min<0 or A_max>cmax or B_min<0 or qB_min<0 or B_max>cmax or C_min<0  or qC_min<0 or C_max>cmax or  D_min<0  or qD_min<0 or D_max>cmax or nanA_max==True or nanA_min==True or nanqA_min==True or nanB_max==True or nanB_min==True or nanqB_min==True or nanC_max==True or nanC_min==True or nanqC_min==True or nanD_max==True or nanD_min==True or nanqD_min==True:
       print('Warning : It was not converge. Please try to set smaller Time Step Length or Space Step Length.')              
       Material_output='Material : ' + str(No_or_Name)
       if Material_output not in G:   
          G.append(Material_output)

#OUTPUT编号
       if "Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length." not in G:
          G.append('Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length.')
          
       filename_data_error1 = "OUTPUT_" + str(No_or_Name) + ".txt"
       output_data_error1=open('OUTPUT/%s'%(filename_data_error1),'w')#带有变量，字符中带有变量，‘%s'%(变量)
       for l in range(len(G)):
           output_data_error1.write(str(G[l]))
           #output_data_error1.write("\t")
           output_data_error1.write("\n")
       output_data_error1.close()

       print('The output files have been finished')
    
    if A_min==0 and  qA_min==0 and A_max<=cmax and B_min==0 and  qB_min==0 and B_max<=cmax and C_min==0 and  qC_min==0 and C_max<=cmax and D_min==0 and qD_min==0 and D_max<=cmax :
       
       if BTTC=='No':
                    
          if yA !=0 :
             DATA_A=A[Z,:]/CA_0
             filename_A = "OUTPUT_" + str(No_or_Name) + "_" + A_name +".txt"
             output_A=open('DATA/%s'%(filename_A),'w')
             for l in range(len(DATA_A)):
                 output_A.write(str(DATA_A[l]))
                 #output_A.write("\t")#空4个字符 可以不加
                 output_A.write("\n")#\n换行
             output_A.close() 
                
          if yB !=0 :
             DATA_B=B[Z,:]/CB_0 
             filename_B = "OUTPUT_" + str(No_or_Name) + "_" + B_name +".txt"
             output_B=open('DATA/%s'%(filename_B),'w')
             for l in range(len(DATA_B)):
                 output_B.write(str(DATA_B[l]))
                 #output_B.write("\t")#空4个字符 可以不加
                 output_B.write("\n")#\n换行
             output_B.close()            

          if yC !=0 :
             DATA_C=C[Z,:]/CC_0 
             filename_C = "OUTPUT_" + str(No_or_Name) + "_" + C_name +".txt"
             output_C=open('DATA/%s'%(filename_C),'w')
             for l in range(len(DATA_C)):
                 output_C.write(str(DATA_C[l]))
                 #output_C.write("\t")#空4个字符 可以不加
                 output_C.write("\n")#\n换行
             output_C.close()    
                
          if yD !=0 : 
             DATA_D=D[Z,:]/CD_0 
             filename_D = "OUTPUT_" + str(No_or_Name) + "_" + D_name +".txt" 
             output_D=open('DATA/%s'%(filename_D),'w')
             for l in range(len(DATA_D)):
                 output_D.write(str(DATA_D[l]))
                 #output_D.write("\t")#空4个字符 可以不加
                 output_D.write("\n")#\n换行
             output_D.close()    

#h        
          if unit_of_time=='h':     
             filename_TIME = "OUTPUT_" + str(No_or_Name) + "_TIME_hour.txt"  
             TIME_OUTPUT=space_time
             output_TIME=open('DATA/%s'%(filename_TIME),'w')#带有变量，字符中带有变量，‘%s'%(变量) 'C:/Users/Eden/Desktop/%s'%(filename)
             for l in range(len(TIME_OUTPUT)):
                 output_TIME.write(str(TIME_OUTPUT[l]))
                 #output_TIME.write("\t")#空4个字符 可以不加
                 output_TIME.write("\n")#\n换行
             output_TIME.close()
#min        
          if unit_of_time=='min':     
             filename_TIME = "OUTPUT_" + str(No_or_Name) + "_TIME_minute.txt"  
             TIME_OUTPUT=space_time*60
             output_TIME=open('DATA/%s'%(filename_TIME),'w')#带有变量，字符中带有变量，‘%s'%(变量) 'C:/Users/Eden/Desktop/%s'%(filename)
             for l in range(len(TIME_OUTPUT)):
                 output_TIME.write(str(TIME_OUTPUT[l]))
                 #output_TIME.write("\t")#空4个字符 可以不加
                 output_TIME.write("\n")#\n换行
             output_TIME.close()
#s        
          if unit_of_time=='s':     
             filename_TIME = "OUTPUT_" + str(No_or_Name) + "_TIME_second.txt"  
             TIME_OUTPUT=space_time*3600
             output_TIME=open('DATA/%s'%(filename_TIME),'w')#带有变量，字符中带有变量，‘%s'%(变量) 'C:/Users/Eden/Desktop/%s'%(filename)
             for l in range(len(TIME_OUTPUT)):
                 output_TIME.write(str(TIME_OUTPUT[l]))
                 #output_TIME.write("\t")#空4个字符 可以不加
                 output_TIME.write("\n")#\n换行
             output_TIME.close()
             
       if BTTC=='Yes':
        
          if dC_A<0 or dC_B<0 or dC_C<0 or dC_D<0 :             
             print('Warning: The setting time is not long enough. Please set larger Time Steps for enough time.')        
             Material_output='Material : ' + str(No_or_Name)
             if Material_output not in G:   
                G.append(Material_output)


             if "Warning: The setting time is not long enough. Please set larger Time Steps for enough time." not in G:
                G.append('Warning: The setting time is not long enough. Please set larger Time Steps for enough time.')
                
             filename_data_error2 = "OUTPUT_" + str(No_or_Name) + ".txt"
             output_data_error2=open('OUTPUT/%s'%(filename_data_error2 ),'w')#带有变量，字符中带有变量，‘%s'%(变量)             
             for l in range(len(G)):
                 output_data_error2.write(str(G[l]))
                 #output_data_error2.write("\t")
                 output_data_error2.write("\n")
             output_data_error2.close()
             
          if dC_A>=0 and dC_B>=0 and dC_C>=0 and dC_D>=0 : 
                    
             if yA !=0 :
                DATA_A=A[Z,:]/CA_0
                filename_A = "OUTPUT_" + str(No_or_Name) + "_" + A_name +".txt"
                output_A=open('DATA/%s'%(filename_A),'w')
                for l in range(len(DATA_A)):
                    output_A.write(str(DATA_A[l]))
                    #output_A.write("\t")#空4个字符 可以不加
                    output_A.write("\n")#\n换行
                output_A.close() 
                
             if yB !=0 :
                DATA_B=B[Z,:]/CB_0 
                filename_B = "OUTPUT_" + str(No_or_Name) + "_" + B_name +".txt" 
                output_B=open('DATA/%s'%(filename_B),'w')
                for l in range(len(DATA_B)):
                    output_B.write(str(DATA_B[l]))
                    #output_B.write("\t")#空4个字符 可以不加
                    output_B.write("\n")#\n换行
                output_B.close()            

             if yC !=0 :
                DATA_C=C[Z,:]/CC_0 
                filename_C = "OUTPUT_" + str(No_or_Name) + "_" + C_name +".txt" 
                output_C=open('DATA/%s'%(filename_C),'w')
                for l in range(len(DATA_C)):
                    output_C.write(str(DATA_C[l]))
                    #output_C.write("\t")#空4个字符 可以不加
                    output_C.write("\n")#\n换行
                output_C.close()    
                
             if yD !=0 : 
                DATA_D=D[Z,:]/CD_0 
                filename_D = "OUTPUT_" + str(No_or_Name) + "_" + D_name +".txt"
                output_D=open('DATA/%s'%(filename_D),'w')
                for l in range(len(DATA_D)):
                    output_D.write(str(DATA_D[l]))
                    #output_D.write("\t")#空4个字符 可以不加
                    output_D.write("\n")#\n换行
                output_D.close()    
             
#h        
          if unit_of_time=='h':     
             filename_TIME_h = "OUTPUT_" + str(No_or_Name) + "_TIME_hour.txt"  
             TIME_OUTPUT_h=space_time
             output_TIME_h=open('DATA/%s'%(filename_TIME_h),'w')#带有变量，字符中带有变量，‘%s'%(变量) 'C:/Users/Eden/Desktop/%s'%(filename)
             for l in range(len(TIME_OUTPUT_h)):
                 output_TIME_h.write(str(TIME_OUTPUT_h[l]))
                 #output_TIME_h.write("\t")#空4个字符 可以不加
                 output_TIME_h.write("\n")#\n换行
             output_TIME_h.close()
#min        
          if unit_of_time=='min':     
             filename_TIME_min = "OUTPUT_" + str(No_or_Name) + "_TIME_minute.txt"  
             TIME_OUTPUT_min=space_time*60
             output_TIME_min=open('DATA/%s'%(filename_TIME_min),'w')#带有变量，字符中带有变量，‘%s'%(变量) 'C:/Users/Eden/Desktop/%s'%(filename)
             for l in range(len(TIME_OUTPUT_min)):
                 output_TIME_min.write(str(TIME_OUTPUT_min[l]))
                 #output_TIME_min.write("\t")#空4个字符 可以不加
                 output_TIME_min.write("\n")#\n换行
             output_TIME_min.close()
#s        
          if unit_of_time=='s':     
             filename_TIME_s = "OUTPUT_" + str(No_or_Name) + "_TIME_second.txt"  
             TIME_OUTPUT_s=space_time*3600
             output_TIME_s=open('DATA/%s'%(filename_TIME_s),'w')#带有变量，字符中带有变量，‘%s'%(变量) 'C:/Users/Eden/Desktop/%s'%(filename)
             for l in range(len(TIME_OUTPUT_s)):
                 output_TIME_s.write(str(TIME_OUTPUT_s[l]))
                 #output_TIME_s.write("\t")#空4个字符 可以不加
                 output_TIME_s.write("\n")#\n换行
             output_TIME_s.close()   
          
               
    return print('Finish')

if __name__ == "__main__" :
   DATA_output() #import时不会被启用
   
def Figure_output(unit_of_time='h',
                  save_figure='Yes',
                  save_type='jpg',
                  dpi=600,
                  linestyle_A='-',
                  linestyle_B='-',
                  linestyle_C='-',
                  linestyle_D='-',
                  linecolor_A='b',
                  linecolor_B='r',
                  linecolor_C='g',
                  linecolor_D='y',
                  plotmarker_A='^',
                  plotmarker_B='^',
                  plotmarker_C='^',
                  plotmarker_D='^',
                  plotcolor_A='b',
                  plotcolor_B='r',
                  plotcolor_C='g',
                  plotcolor_D='y'):
    
    if system == 'nt' :
       from matplotlib import pyplot as plt
    else:
       import matplotlib
       matplotlib.use('Agg')
       from matplotlib import pyplot as plt
       
    print('Begin to draw')
    
    if A_min<0  or qA_min<0 or A_max>cmax or B_min<0 or qB_min<0 or B_max>cmax or C_min<0  or qC_min<0 or C_max>cmax or  D_min<0  or qD_min<0 or D_max>cmax or nanA_max==True or nanA_min==True or nanqA_min==True or nanB_max==True or nanB_min==True or nanqB_min==True or nanC_max==True or nanC_min==True or nanqC_min==True or nanD_max==True or nanD_min==True or nanqD_min==True:
       print('Warning : It was not converge. Please try to set smaller Time Step Length or Space Step Length.')       
       Material_output='Material : ' + str(No_or_Name)
       if Material_output not in G:   
          G.append(Material_output)


       if "Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length." not in G:
          G.append('Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length.')
          
       print('The output files have been finished')
    
    if A_min==0 and  qA_min==0 and A_max<=cmax and B_min==0 and  qB_min==0 and B_max<=cmax and C_min==0 and  qC_min==0 and C_max<=cmax and D_min==0 and qD_min==0 and D_max<=cmax :
       
        if BTTC=='No':
#绘图                         
           if yA ==0 and yB !=0 and yC !=0 and yD !=0 :
              Y_MAX=(B_max/CB_0,C_max/CC_0,D_max/CD_0)
                
           if yA !=0 and yB ==0 and yC !=0 and yD !=0 :
              Y_MAX=(A_max/CA_0,C_max/CC_0,D_max/CD_0)
                
           if yA !=0 and yB !=0 and yC ==0 and yD !=0 :
              Y_MAX=(A_max/CA_0,B_max/CB_0,D_max/CD_0)
               
           if yA !=0 and yB !=0 and yC !=0 and yD ==0 :
              Y_MAX=(A_max/CA_0,B_max/CB_0,C_max/CC_0)
              
           if yA ==0 and yB ==0 and yC !=0 and yD !=0 :
              Y_MAX=(C_max/CC_0,D_max/CD_0)  
              
           if yA ==0 and yB !=0 and yC ==0 and yD !=0 :
              Y_MAX=(B_max/CB_0,D_max/CD_0)   
           
           if yA ==0 and yB !=0 and yC !=0 and yD ==0 :
              Y_MAX=(B_max/CB_0,C_max/CC_0)    
           
           if yA !=0 and yB ==0 and yC ==0 and yD !=0 :
              Y_MAX=(A_max/CA_0,D_max/CD_0)  
           
           if yA !=0 and yB ==0 and yC !=0 and yD ==0 :
              Y_MAX=(A_max/CA_0,C_max/CC_0)  
              
           if yA !=0 and yB !=0 and yC ==0 and yD ==0 :
              Y_MAX=(A_max/CA_0,B_max/CB_0)
              
           if yA ==0 and yB ==0 and yC ==0 and yD !=0 :
              Y_MAX=(D_max/CD_0)   
              
           if yA ==0 and yB ==0 and yC !=0 and yD ==0 :
              Y_MAX=(C_max/CC_0)   
              
           if yA ==0 and yB !=0 and yC ==0 and yD ==0 :
              Y_MAX=(B_max/CB_0) 
              
           if yA !=0 and yB ==0 and yC ==0 and yD ==0 :
              Y_MAX=(A_max/CA_0)     
#h            
           if unit_of_time=='h' :                 
              plt.figure()
                
              if yA !=0 :
                 plt.plot(space_time,A[Z,:]/CA_0,ls=linestyle_A,c=linecolor_A,label=A_name) #全部文字前后添加$会变斜体
                 Y_MAX=Y_MAX+0.125                   
              if yB !=0 :                     
                 plt.plot(space_time,B[Z,:]/CB_0,ls=linestyle_B,c=linecolor_B,label=B_name)  
                 Y_MAX=Y_MAX+0.125   
              if yC !=0 :              
                 plt.plot(space_time,C[Z,:]/CC_0,ls=linestyle_C,c=linecolor_C,label=C_name)  
                 Y_MAX=Y_MAX+0.125   
              if yD !=0 :   
                 plt.plot(space_time,D[Z,:]/CD_0,ls=linestyle_D,c=linecolor_D,label=D_name)  
                 Y_MAX=Y_MAX+0.125   
                                         
              plt.ylabel('$C_i$/$C_0$')
              plt.xlabel('time/h')
              plt.axis([0,t,0,round(Y_MAX,1)])#xy轴范围 round(a,1) a取1位小数
              plt.legend()
              if save_figure=='Yes':
                 Figure_name='FIGURE/Breakthrough_curve.' + save_type
                 plt.savefig(Figure_name,dpi=dpi)                 
              if save_figure=='No':
                 if system == 'nt' :
                    plt.show()
                 else:
                    G.append('Warning: invalid parameter for Figure_output() in system expect window.')
                    filename_figure_error1 = "OUTPUT_" + str(No_or_Name) + ".txt"
                    output_figure_error1=open('OUTPUT/%s'%(filename_figure_error1),'w')#带有变量，字符中带有变量，‘%s'%(变量)
                    for l in range(len(G)):
                        output_figure_error1.write(str(G[l]))
                        #output_figure_error1.write("\t")
                        output_figure_error1.write("\n")
                    output_figure_error1.close()
#min
           if unit_of_time=='min' :                 
              plt.figure()
                
              if yA !=0 :
                 plt.plot(space_time*60,A[Z,:]/CA_0,ls=linestyle_A,c=linecolor_A,label=A_name) #全部文字前后添加$会变斜体
                 Y_MAX=Y_MAX+0.125                   
              if yB !=0 :                     
                 plt.plot(space_time*60,B[Z,:]/CB_0,ls=linestyle_B,c=linecolor_B,label=B_name)  
                 Y_MAX=Y_MAX+0.125   
              if yC !=0 :              
                 plt.plot(space_time*60,C[Z,:]/CC_0,ls=linestyle_C,c=linecolor_C,label=C_name)  
                 Y_MAX=Y_MAX+0.125   
              if yD !=0 :   
                 plt.plot(space_time*60,D[Z,:]/CD_0,ls=linestyle_D,c=linecolor_D,label=D_name)  
                 Y_MAX=Y_MAX+0.125   
                                         
              plt.ylabel('$C_i$/$C_0$')
              plt.xlabel('time/min')
              plt.axis([0,t*60,0,round(Y_MAX,1)])#xy轴范围 round(a,1) a取1位小数
              plt.legend()
              if save_figure=='Yes':
                 Figure_name='FIGURE/Breakthrough_curve.' + save_type
                 plt.savefig(Figure_name,dpi=dpi)                 
              if save_figure=='No':
                 if system == 'nt' :
                    plt.show()
                 else:
                    G.append('Warning: invalid parameter for Figure_output() in system expect window.')
                    filename_figure_error2 = "OUTPUT_" + str(No_or_Name) + ".txt"
                    output_figure_error2=open('OUTPUT/%s'%(filename_figure_error2),'w')#带有变量，字符中带有变量，‘%s'%(变量)
                    for l in range(len(G)):
                        output_figure_error2.write(str(G[l]))
                        #output_figure_error2.write("\t")
                        output_figure_error2.write("\n")
                    output_figure_error2.close()
#s              
           if unit_of_time=='s' :                 
              plt.figure()
                
              if yA !=0 :
                 plt.plot(space_time*3600,A[Z,:]/CA_0,ls=linestyle_A,c=linecolor_A,label=A_name) #全部文字前后添加$会变斜体
                 Y_MAX=Y_MAX+0.125                   
              if yB !=0 :                     
                 plt.plot(space_time*3600,B[Z,:]/CB_0,ls=linestyle_B,c=linecolor_B,label=B_name)  
                 Y_MAX=Y_MAX+0.125   
              if yC !=0 :              
                 plt.plot(space_time*3600,C[Z,:]/CC_0,ls=linestyle_C,c=linecolor_C,label=C_name)  
                 Y_MAX=Y_MAX+0.125   
              if yD !=0 :   
                 plt.plot(space_time*3600,D[Z,:]/CD_0,ls=linestyle_D,c=linecolor_D,label=D_name)  
                 Y_MAX=Y_MAX+0.125   
                                         
              plt.ylabel('$C_i$/$C_0$')
              plt.xlabel('time/s')
              plt.axis([0,t*3600,0,round(Y_MAX,1)])#xy轴范围 round(a,1) a取1位小数
              plt.legend()
              if save_figure=='Yes':
                 Figure_name='FIGURE/Breakthrough_curve.' + save_type
                 plt.savefig(Figure_name,dpi=dpi)                 
              if save_figure=='No':
                 if system == 'nt' :
                    plt.show()
                 else:
                    G.append('Warning: invalid parameter for Figure_output() in system expect window.')
                    filename_figure_error3 = "OUTPUT_" + str(No_or_Name) + ".txt"
                    output_figure_error3=open('OUTPUT/%s'%(filename_figure_error3),'w')#带有变量，字符中带有变量，‘%s'%(变量)
                    for l in range(len(G)):
                        output_figure_error3.write(str(G[l]))
                        #output_figure_error3.write("\t")
                        output_figure_error3.write("\n")
                    output_figure_error3.close() 
           
        if BTTC=='Yes':   
            
           if dC_A<0 or dC_B<0 or dC_C<0 or dC_D<0 :             
              print('Warning: The setting time is not long enough. Please set larger Time Steps for enough time.')
              Material_output='Material : ' + str(No_or_Name)
              if Material_output not in G:   
                 G.append(Material_output)

              if "Warning: The setting time is not long enough. Please set larger Time Steps for enough time." not in G:
                 G.append('Warning: The setting time is not long enough. Please set larger Time Steps for enough time.')
                 
              filename_figure_error4 = "OUTPUT_" + str(No_or_Name) + ".txt"
              output_figure_error4=open('OUTPUT/%s'%(filename_figure_error4),'w')#带有变量，字符中带有变量，‘%s'%(变量)
              for l in range(len(G)):
                  output_figure_error4.write(str(G[l]))
                  #output_figure_error4.write("\t")
                  output_figure_error4.write("\n")
              output_figure_error4.close()
              
                  
           if dC_A>=0 and dC_B>=0 and dC_C>=0 and dC_D>=0 :
     #绘图  
              if yA ==0 and yB !=0 and yC !=0 and yD !=0 :
                 Y_MAX=(B_max/CB_0,C_max/CC_0,D_max/CD_0)
                   
              if yA !=0 and yB ==0 and yC !=0 and yD !=0 :
                 Y_MAX=(A_max/CA_0,C_max/CC_0,D_max/CD_0)
                   
              if yA !=0 and yB !=0 and yC ==0 and yD !=0 :
                 Y_MAX=(A_max/CA_0,B_max/CB_0,D_max/CD_0)
                  
              if yA !=0 and yB !=0 and yC !=0 and yD ==0 :
                 Y_MAX=(A_max/CA_0,B_max/CB_0,C_max/CC_0)
                 
              if yA ==0 and yB ==0 and yC !=0 and yD !=0 :
                 Y_MAX=(C_max/CC_0,D_max/CD_0)  
                 
              if yA ==0 and yB !=0 and yC ==0 and yD !=0 :
                 Y_MAX=(B_max/CB_0,D_max/CD_0)   
              
              if yA ==0 and yB !=0 and yC !=0 and yD ==0 :
                 Y_MAX=(B_max/CB_0,C_max/CC_0)    
              
              if yA !=0 and yB ==0 and yC ==0 and yD !=0 :
                 Y_MAX=(A_max/CA_0,D_max/CD_0)  
              
              if yA !=0 and yB ==0 and yC !=0 and yD ==0 :
                 Y_MAX=(A_max/CA_0,C_max/CC_0)  
                 
              if yA !=0 and yB !=0 and yC ==0 and yD ==0 :
                 Y_MAX=(A_max/CA_0,B_max/CB_0)
                 
              if yA ==0 and yB ==0 and yC ==0 and yD !=0 :
                 Y_MAX=(D_max/CD_0)   
                 
              if yA ==0 and yB ==0 and yC !=0 and yD ==0 :
                 Y_MAX=(C_max/CC_0)   
                 
              if yA ==0 and yB !=0 and yC ==0 and yD ==0 :
                 Y_MAX=(B_max/CB_0) 
                 
              if yA !=0 and yB ==0 and yC ==0 and yD ==0 :
                 Y_MAX=(A_max/CA_0)  
                 
#h                  
              if unit_of_time=='h' :
                 plt.figure()
                 
                 if yA !=0 :
                    plt.plot(space_time,A[Z,:]/CA_0,ls=linestyle_A,c=linecolor_A,label=A_name) #全部文字前后添加$会变斜体
                    plt.scatter(KNEE_A.elbow,KNEE_A.elbow_y/CA_0,s=200,c=plotcolor_A,marker=plotmarker_A)#穿透时间
                    Y_MAX=Y_MAX+0.125 
                 if yB !=0 :                     
                    plt.plot(space_time,B[Z,:]/CB_0,ls=linestyle_B,c=linecolor_B,label=B_name)
                    plt.scatter(KNEE_B.elbow,KNEE_B.elbow_y/CA_0,s=200,c=plotcolor_B,marker=plotmarker_B)
                    Y_MAX=Y_MAX+0.125 
                 if yC !=0 :              
                    plt.plot(space_time,C[Z,:]/CC_0,ls=linestyle_C,c=linecolor_C,label=C_name)
                    plt.scatter(KNEE_C.elbow,KNEE_C.elbow_y/CA_0,s=200,c=plotcolor_C,marker=plotmarker_C)
                    Y_MAX=Y_MAX+0.125 
                 if yD !=0 :   
                    plt.plot(space_time,D[Z,:]/CD_0,ls=linestyle_D,c=linecolor_D,label=D_name)           
                    plt.scatter(KNEE_D.elbow,KNEE_D.elbow_y/CA_0,s=200,c=plotcolor_D,marker=plotmarker_D)
                    Y_MAX=Y_MAX+0.125 
                     
                 plt.ylabel('$C_i$/$C_0$')
                 plt.xlabel('time/h')
                 plt.axis([0,t,0,round(Y_MAX,1)])#xy轴范围
                 plt.legend()
                 if save_figure=='Yes':
                    Figure_name='FIGURE/Breakthrough_curve.' + save_type
                    plt.savefig(Figure_name,dpi=dpi)                 
                 if save_figure=='No':
                    if system == 'nt' :
                       plt.show()
                    else:
                       G.append('Warning: invalid parameter for Figure_output() in system expect window.')
                       filename_figure_error5 = "OUTPUT_" + str(No_or_Name) + ".txt"
                       output_figure_error5=open('OUTPUT/%s'%(filename_figure_error5),'w')#带有变量，字符中带有变量，‘%s'%(变量)
                       for l in range(len(G)):
                           output_figure_error5.write(str(G[l]))
                           #output_figure_error5.write("\t")
                           output_figure_error5.write("\n")
                       output_figure_error5.close()
#min                 
              if unit_of_time=='min' :
                 plt.figure()
                 
                 if yA !=0 :
                    plt.plot(space_time*60,A[Z,:]/CA_0,ls=linestyle_A,c=linecolor_A,label=A_name) #全部文字前后添加$会变斜体
                    plt.scatter(KNEE_A.elbow*60,KNEE_A.elbow_y/CA_0,s=200,c=plotcolor_A,marker=plotmarker_A)#穿透时间
                    Y_MAX=Y_MAX+0.125 
                 if yB !=0 :                     
                    plt.plot(space_time*60,B[Z,:]/CB_0,ls=linestyle_B,c=linecolor_B,label=B_name)
                    plt.scatter(KNEE_B.elbow*60,KNEE_B.elbow_y/CA_0,s=200,c=plotcolor_B,marker=plotmarker_B)
                    Y_MAX=Y_MAX+0.125 
                 if yC !=0 :              
                    plt.plot(space_time*60,C[Z,:]/CC_0,ls=linestyle_C,c=linecolor_C,label=C_name)
                    plt.scatter(KNEE_C.elbow*60,KNEE_C.elbow_y/CA_0,s=200,c=plotcolor_C,marker=plotmarker_C)
                    Y_MAX=Y_MAX+0.125 
                 if yD !=0 :   
                    plt.plot(space_time*60,D[Z,:]/CD_0,ls=linestyle_D,c=linecolor_D,label=D_name)           
                    plt.scatter(KNEE_D.elbow*60,KNEE_D.elbow_y/CA_0,s=200,c=plotcolor_D,marker=plotmarker_D)
                    Y_MAX=Y_MAX+0.125 
                     
                 plt.ylabel('$C_i$/$C_0$')
                 plt.xlabel('time/MIN')
                 plt.axis([0,t*60,0,round(Y_MAX,1)])#xy轴范围
                 plt.legend()
                 if save_figure=='Yes':
                    Figure_name='FIGURE/Breakthrough_curve.' + save_type
                    plt.savefig(Figure_name,dpi=dpi)                 
                 if save_figure=='No':
                    if system == 'nt' :
                       plt.show()
                    else:
                       G.append('Warning: invalid parameter for Figure_output() in system expect window.')
                       filename_figure_error6 = "OUTPUT_" + str(No_or_Name) + ".txt"
                       output_figure_error6=open('OUTPUT/%s'%(filename_figure_error6),'w')#带有变量，字符中带有变量，‘%s'%(变量)
                       for l in range(len(G)):
                           output_figure_error6.write(str(G[l]))
                           #output_figure_error6.write("\t")
                           output_figure_error6.write("\n")
                       output_figure_error6.close()
#s                 
              if unit_of_time=='s' :
                 plt.figure()
                 
                 if yA !=0 :
                    plt.plot(space_time*3600,A[Z,:]/CA_0,ls=linestyle_A,c=linecolor_A,label=A_name) #全部文字前后添加$会变斜体
                    plt.scatter(KNEE_A.elbow*3600,KNEE_A.elbow_y/CA_0,s=200,c=plotcolor_A,marker=plotmarker_A)#穿透时间
                    Y_MAX=Y_MAX+0.125 
                 if yB !=0 :                     
                    plt.plot(space_time*3600,B[Z,:]/CB_0,ls=linestyle_B,c=linecolor_B,label=B_name)
                    plt.scatter(KNEE_B.elbow*3600,KNEE_B.elbow_y/CA_0,s=200,c=plotcolor_B,marker=plotmarker_B)
                    Y_MAX=Y_MAX+0.125 
                 if yC !=0 :              
                    plt.plot(space_time*3600,C[Z,:]/CC_0,ls=linestyle_C,c=linecolor_C,label=C_name)
                    plt.scatter(KNEE_C.elbow*3600,KNEE_C.elbow_y/CA_0,s=200,c=plotcolor_C,marker=plotmarker_C)
                    Y_MAX=Y_MAX+0.125 
                 if yD !=0 :   
                    plt.plot(space_time*3600,D[Z,:]/CD_0,ls=linestyle_D,c=linecolor_D,label=D_name)           
                    plt.scatter(KNEE_D.elbow*3600,KNEE_D.elbow_y/CA_0,s=200,c=plotcolor_D,marker=plotmarker_D)
                    Y_MAX=Y_MAX+0.125 
                     
                 plt.ylabel('$C_i$/$C_0$')
                 plt.xlabel('time/s')
                 plt.axis([0,t*3600,0,round(Y_MAX,1)])#xy轴范围
                 plt.legend()
                 if save_figure=='Yes':
                    Figure_name='FIGURE/Breakthrough_curve.' + save_type
                    plt.savefig(Figure_name,dpi=dpi)                 
                 if save_figure=='No':
                    if system == 'nt' :
                       plt.show()
                    else:
                       G.append('Warning: invalid parameter for Figure_output() in system expect window.')
                       filename_figure_error7 = "OUTPUT_" + str(No_or_Name) + ".txt"
                       output_figure_error7=open('OUTPUT/%s'%(filename_figure_error7),'w')#带有变量，字符中带有变量，‘%s'%(变量)
                       for l in range(len(G)):
                           output_figure_error7.write(str(G[l]))
                           #output_figure_error7.write("\t")
                           output_figure_error7.write("\n")
                       output_figure_error7.close()                 

            
    return print('Finish')
    
if __name__ == "__main__" :
   Figure_output() #import时不会被启用    
    

 
          

         
             

      