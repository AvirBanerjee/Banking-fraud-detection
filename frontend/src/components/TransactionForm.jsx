import { useState } from "react";
import { predictTransaction } from "../api/api";
import toast from "react-hot-toast";

export default function TransactionForm({ setResult }) {
  const [form, setForm] = useState({
    user_id: "",
    amount: "",
    location: "",
    device: "",
    time: "",
    is_international: false,
    avg_amount: "",
    usual_location: "",
    usual_time: ""
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm({
      ...form,
      [name]: type === "checkbox" ? checked : value
    });
  };

  const validateForm = () => {
    if (!form.user_id || !form.amount || !form.time) {
      toast.error("Please fill required fields");
      return false;
    }

    if (!form.time.includes(":")) {
      toast.error("Time must be in HH:MM format");
      return false;
    }

    if (!form.usual_time.includes("-")) {
      toast.error("Use format: 10:00-18:00 or 4 pm-10 pm");
      return false;
    }

    return true;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) return;

    const payload = {
      user_id: form.user_id,
      amount: Number(form.amount),
      location: form.location,
      device: form.device,
      time: form.time,
      transaction_type: "online",
      is_international: form.is_international,
      user_history: {
        avg_amount: Number(form.avg_amount || 0),
        usual_location: form.usual_location,
        usual_time: form.usual_time
      }
    };

    try {
      toast.loading("Analyzing transaction...");

      const res = await predictTransaction(payload);

      toast.dismiss();
      toast.success("Prediction successful ✅");

      setResult(res.data);

    } catch (err) {
      toast.dismiss();

      const msg =
        err.response?.data?.detail ||
        err.message ||
        "API failed";

      toast.error(msg);
      console.error(err);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-2xl shadow-lg space-y-4">
      <h2 className="text-xl font-bold">Transaction Details</h2>

      <input className="input" name="user_id" placeholder="User ID" onChange={handleChange} />
      <input className="input" name="amount" placeholder="Amount" onChange={handleChange} />
      <input className="input" name="location" placeholder="Location" onChange={handleChange} />
      <input className="input" name="device" placeholder="Device" onChange={handleChange} />
      <input className="input" name="time" placeholder="Time (HH:MM)" onChange={handleChange} />

      <label className="flex gap-2">
        <input type="checkbox" name="is_international" onChange={handleChange} />
        International Transaction
      </label>

      <h3 className="font-semibold">User History</h3>

      <input className="input" name="avg_amount" placeholder="Avg Amount" onChange={handleChange} />
      <input className="input" name="usual_location" placeholder="Usual Location" onChange={handleChange} />
      <input className="input" name="usual_time" placeholder="10:00-18:00 or 4 pm-10 pm" onChange={handleChange} />

      <button className="bg-blue-600 text-white px-4 py-2 rounded-xl hover:bg-blue-700 w-full">
        Predict
      </button>
    </form>
  );
}