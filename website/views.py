from flask import Blueprint, render_template, flash, request
import pickle
from back import fish_ratio, average_weight, global_average_weight, global_average_ratio, clean_fish

data_dir = "./website/data/downloaded_data/"
size_dict = {}
name_dict = {}
number_of_ranks = 5


with open(data_dir + "SIZES.pkl", 'rb') as f:
    size_dict = pickle.load(f)
with open(data_dir + "NAMES.pkl", 'rb') as g:
    name_dict = pickle.load(g)
with open(data_dir + "FISH.pkl", 'rb') as h:
    fish_list = pickle.load(h)

avrg_weights = {}
for fish in fish_list:
    avrg_weights[fish] = global_average_weight(data_dir, fish)
avrg_ratios = {}
for fish in fish_list:
    avrg_ratios[fish] = global_average_ratio(data_dir, fish, size_dict)


views = Blueprint('views', __name__)

@views.route('/home', methods=['POST', 'GET'])
def about():
    return render_template("home.html")

@views.route('/output', methods=['POST', 'GET'])
def output():
    return render_template("output.html")

@views.route('/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        inputed_area = request.form.get('areas')
        inputed_fish = request.form.get('fish')
        if inputed_fish:
            fish_cl = clean_fish[inputed_fish]
            if not inputed_area:
                flash("Vyber revír!",category='success')
            if inputed_area == "999":
                for fish in fish_list:
                    if fish == inputed_fish:
                        best_fish_dict = {}
                        for key, value in name_dict.items():
                            if average_weight(key, fish):
                                best_fish_dict[key] = average_weight(key, fish)
                        try:
                            max_avrg_weight = max(best_fish_dict.values())
                        except Exception:
                            continue
                        sorted_dict = sorted(best_fish_dict.items(), key=lambda x: x[1], reverse=True)
                        reversed_dict = sorted(best_fish_dict.items(), key=lambda x: x[1], reverse=False)
                        area_outp = []
                        weight_outp = []
                        counter = 0
                        for value in sorted_dict:
                            counter += 1
                            area_outp.append(name_dict[value[0]])
                            weight_outp.append(round(value[1], 2))
                            if counter == number_of_ranks:
                                break
                        area_outp_b = []
                        weight_outp_b = []
                        counter = 0
                        for value in reversed_dict:
                            counter += 1
                            area_outp_b.append(name_dict[value[0]])
                            weight_outp_b.append(round(value[1], 2))
                            if counter == number_of_ranks:
                                break

                        return render_template('output_all.html', inputed_fish=fish_cl, a_out = area_outp, a_out_w=area_outp_b,
                                               w_out=weight_outp, w_out_w=weight_outp_b, formul_1 = " průměrné váhy", formul_2 = "kg")


            if inputed_area == "777":
                for fish in fish_list:
                    if fish == inputed_fish:
                        best_ratio_dict = {}
                        for key, value in name_dict.items():
                            if fish_ratio(key, fish, size_dict[key]):
                                best_ratio_dict[key] = fish_ratio(key, fish, size_dict[key])
                        try:
                            max_avrg_ratio = max(best_ratio_dict.values())
                        except Exception:
                            continue
                        sorted_dict = sorted(best_ratio_dict.items(), key=lambda x: x[1], reverse=True)
                        reversed_dict = sorted(best_ratio_dict.items(), key=lambda x: x[1], reverse=False)

                        area_outp = []
                        ratio_outp = []
                        counter = 0
                        for value in sorted_dict:
                            counter += 1
                            area_outp.append(name_dict[value[0]])
                            ratio_outp.append(round(value[1], 2))
                            if counter == number_of_ranks:
                                break
                        area_outp_b = []
                        ratio_outp_b = []
                        counter = 0
                        for value in reversed_dict:
                            counter += 1
                            area_outp_b.append(name_dict[value[0]])
                            ratio_outp_b.append(round(value[1], 2))
                            if counter == number_of_ranks:
                                break

                        return render_template('output_all.html', inputed_fish=fish_cl, a_out=area_outp, a_out_w=area_outp_b,
                                               w_out=ratio_outp, w_out_w=ratio_outp_b, formul_1 = "kusů", formul_2 = "kusů / hektar / rok")


            else:
                for key, value in name_dict.items():
                    if key == inputed_area:
                        name = value
                        number = key
                        size = size_dict[key]

                        o_weight = ""
                        if average_weight(key, inputed_fish):
                            weight = round(average_weight(key, inputed_fish), 2)
                            if average_weight(key, inputed_fish) > avrg_weights[inputed_fish]:
                                o_weight = "více"
                            else:
                                o_weight = "méně"
                            avrg_w = round(avrg_weights[inputed_fish], 3)

                        o_ratio = ""
                        if fish_ratio(key, inputed_fish, size_dict[key]):
                            ratio = round(fish_ratio(key, inputed_fish, size_dict[key]), 3)
                            if float(fish_ratio(key, inputed_fish, size_dict[key]) > float(avrg_ratios[inputed_fish])):
                                o_ratio = "více"
                            else:
                                o_ratio = "méně"
                            avrg_r = round(avrg_ratios[inputed_fish], 2)
                            return render_template('output.html', inputed_fish=fish_cl, size=size, name=name, number=number,
                                                   weight=weight, ratio=ratio, o_weight=o_weight, o_ratio=o_ratio, avrg_w=avrg_w,
                                                   avrg_r=avrg_r)
                        else:
                            flash(f"Zatím žádný záznam:  {fish_cl} - {value}", category='success')
        else:
            flash("Vyber rybu!", category='success')

                
    return render_template("calc.html")