from flask import Flask, request, render_template

app = Flask(__name__)

# Cơ sở dữ liệu nhân viên
employees = {
    "1": {"name": "John Smith", "department": "Sales"},
    "2": {"name": "Jane Doe", "department": "Marketing"},
}

# Cơ sở dữ liệu check-in/check-out
check_in_out = {}

# Trang chủ
@app.route("/")
def home():
    return render_template("home.html")

# Check-in
@app.route("/check-in", methods=["POST"])
def check_in():
    employee_id = request.form.get("employee_id")
    now = datetime.datetime.now()
    check_in_out[employee_id] = {"check_in": now}
    return redirect(url_for("home"))

# Check-out
@app.route("/check-out", methods=["POST"])
def check_out():
    employee_id = request.form.get("employee_id")
    now = datetime.datetime.now()
    check_in_out[employee_id]["check_out"] = now
    return redirect(url_for("home"))

# Tạo báo cáo
@app.route("/report")
def report():
    with open("report.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Mã nhân viên", "Tên nhân viên", "Phòng ban", "Ngày", "Giờ vào", "Giờ ra"])
        for employee_id, data in check_in_out.items():
            employee = employees[employee_id]
            date = data["check_in"].date()
            time_in = data["check_in"].time()
            time_out = data["check_out"].time()
            writer.writerow([employee_id, employee["name"], employee["department"], date, time_in, time_out])
    return send_file("report.csv", as_attachment=True)

if __name__ == "__main__":
    app.run()