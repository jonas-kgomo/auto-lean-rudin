import data.real.basic
import data.rat.basic

open_locale classical

theorem archimedean_property (x y : ℝ) (hx : 0 < x) : ∃ n : ℕ, y < n * x :=
begin
  by_contra h,
  push_neg at h,
  let A := {n : ℕ | n * x ≤ y},
  have hA : ∀ n : ℕ, n ∈ A,
  { intro n, exact h n },
  obtain ⟨α, hαA, ⟨⟩⟩ : ∃ α, is_lub (λ n : ℕ, n * x) α,
  { exact real.exists_is_lub ⟨0, by norm_num⟩ },
  let β := α - x,
  have β_lt_α : β < α := sub_lt_self _ hx,
  have hβ : ∃ n : ℕ, β < n * x := by simp [not_forall, β_lt_α, sub_eq_iff_eq_add, add_comm] at hαA; exact hαA,
  obtain ⟨m, hβ⟩ := hβ,
  have : α < (m + 1) * x,
  { calc α = β + x        : by rw sub_add_cancel
        ... < m * x + x   : by { rw ← hβ, exact add_lt_add_right hβ x }
        ... = (m + 1) * x : by ring },
  exact hαA this
end

theorem density_of_rationals (x y : ℝ) (h : x < y) : ∃ p : ℚ, x < p ∧ p < y :=
begin
  have h' := sub_pos.mpr h,
  obtain ⟨n, hn⟩ := archimedean_property (y - x) 1 h',
  have h₁ : n * (y - x) > 1 := hn,
  obtain ⟨m, hm⟩ := archimedean_property x ((n * y - m) / n) (div_pos (lt_of_le_of_lt zero_le_one (lt_mul_right_of_lt_div h₁)) (nat.cast_pos.mpr n.pos)),
  let q := m / n : ℚ,
  use q,
  split,
  { exact div_lt_of_mul_lt (nat.cast_pos.mpr n.pos) (lt_of_sub_left_div_lt hmn) },
  { exact div_lt_of_mul_lt (nat.cast_pos.mpr n.pos) h₁ }
end