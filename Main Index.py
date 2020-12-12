""" Recieve And Process """
import faculty as fac

def main():
    """ Recieve A Score """
    score = {
        "GAT": float(input("GAT: ")),
        "GAT TH": float(input("GAT1: ")),
        "GAT ENG": float(input("GAT2: ")),
        "PAT1": float(input("PAT1: ")),
        "PAT2": float(input("PAT2: ")),
        "PAT3": float(input("PAT3: ")),
        "PAT4": float(input("PAT4: ")),
        "PAT5": float(input("PAT5: ")),
        "PAT6": float(input("PAT6: ")),
        "PAT7": float(input("PAT7: "))
    }
    faculty_branch = {
        "Order 1": [input(), input()],
        "Order 2": [input(), input()],
        "Order 3": [input(), input()],
        "Order 4": [input(), input()],
        "Order 5": [input(), input()]
    }
    faculty_score = []

    for order in faculty_branch:
        if faculty_branch[order][0] == "คณะวิศวกรรมศาสตร์":
            result = fac.engineering(score["GAT"], score["PAT1"], score["PAT3"])
            print(result)
        elif faculty_branch[order][0] == "คณะวิศวกรรมศาสตร์(หลักสูตรนานาชาติ)":
            result = fac.engineering_national(score["GAT TH"], score["GAT ENG"], score["PAT1"], score["PAT3"])
            print(result)
        elif faculty_branch[order][0] == "คณะวิทยาศาสตร์":
            result = fac.science(score["GAT"], score["PAT1"], score["PAT2"], faculty_branch[order][1])
            print(result)
        elif faculty_branch[order][0] == "คณะสถาปัตยกรรมศาสตร์":
            result = fac.architecture(score["GAT"], score["PAT4"], score["PAT6"], faculty_branch[order][1])
            print(result)
        elif faculty_branch[order][0] == "คณะบริหารธุรกิจ":
            result = fac.business_administration(score["GAT"], score["PAT1"])
            print(result)
        elif faculty_branch[order][0] == "คณะเทคโนโลยีสารสนเทศ":
            result = fac.information_technology(score["GAT"], score["PAT1"])
            print(result)
        elif faculty_branch[order][0] == "คณะอุตสาหกรรมอาหาร":
            result = fac.food_industry(score["GAT"], score["PAT1"], score["PAT2"], faculty_branch[order][1])
            print(result)
        elif faculty_branch[order][0] == "คณะครุศาสตร์อุตสาหกรรมและเทคโนโลยี":
            result = fac.education_industry_technology(score["GAT"], score["PAT2"], score["PAT3"], score["PAT4"], score["PAT5"], faculty_branch[order][1])
            print(result)
        elif faculty_branch[order][0] == "คณะเทคโนโลยีการเกษตร":
            result = fac.agricultural_technology(score["GAT TH"], score["PAT1"], score["PAT2"])
            print(result)
        elif faculty_branch[order][0] == "วิทยาลัยนวัตกรรมการผลิตขั้นสูง":
            result = fac.engineering_manufacturing(score["PAT1"], score["PAT2"], score["PAT3"])
            print(result)
        elif faculty_branch[order][0] == "วิทยาลัยนาโนเทคโนโลยีพระจอมเกล้าลาดกระบัง":
            result = fac.bachelor_technokmitl(score["GAT"], score["PAT1"], score["PAT2"])
            print(result)
        elif faculty_branch[order][0] == "วิทยาลัยอุตสาหกรรมการบินนานาชาติ":
            result = fac.aviation_industry(score["GAT"], score["PAT1"], score["PAT3"], faculty_branch[order][1])
            print(result)
        elif faculty_branch[order][0] == "วิทยาลัยวิศวกรรมสังคีต":
            result = fac.imse(score["GAT"], score["PAT1"], score["PAT3"])
            print(result)
        elif faculty_branch[order][0] == "วิทยาเขตชุมพรเขตรอุดมศักดิ์ จังหวัดชุมพร":
            result = fac.kmitl_pcc(score["GAT"], score["PAT1"], score["PAT2"], score["PAT3"], faculty_branch[order][0])
            print(result)

main()
