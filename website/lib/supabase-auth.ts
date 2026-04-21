import { supabase } from "./supabase";
import * as bcrypt from "bcryptjs";

export async function authenticateUser(email: string, password: string) {
  try {
    // Get user from database
    const { data: user, error } = await supabase
      .from("users")
      .select("*")
      .eq("email", email)
      .single();

    if (error || !user) {
      return null;
    }

    // Compare password
    const isPasswordValid = await bcrypt.compare(password, user.password_hash);
    if (!isPasswordValid) {
      return null;
    }

    // Check if month has reset
    const lastReset = new Date(user.month_reset_date);
    const now = new Date();
    if (
      lastReset.getMonth() !== now.getMonth() ||
      lastReset.getFullYear() !== now.getFullYear()
    ) {
      // Reset WU sessions for new month
      await supabase
        .from("users")
        .update({
          wu_sessions_this_month: 0,
          month_reset_date: now.toISOString(),
        })
        .eq("id", user.id);

      user.wu_sessions_this_month = 0;
    }

    return {
      id: user.id,
      email: user.email,
      name: user.name,
      plan: user.plan,
      isAdmin: user.is_admin,
      wuSessionsThisMonth: user.wu_sessions_this_month,
      departmentId: user.department_id,
    };
  } catch (error) {
    console.error("Auth error:", error);
    return null;
  }
}

export async function registerUser(
  email: string,
  password: string,
  name: string,
  inviteCode?: string
) {
  try {
    // Check if user exists
    const { data: existing } = await supabase
      .from("users")
      .select("id")
      .eq("email", email)
      .single();

    if (existing) {
      throw new Error("User already exists");
    }

    // Hash password
    const salt = await bcrypt.genSalt(10);
    const passwordHash = await bcrypt.hash(password, salt);

    // Find department if invite code provided
    let departmentId = null;
    let plan = "FREE";

    if (inviteCode) {
      const { data: department } = await supabase
        .from("departments")
        .select("id")
        .eq("invite_code", inviteCode)
        .eq("active", true)
        .single();

      if (department) {
        departmentId = department.id;
        plan = "DEPARTMENT";
      }
    }

    // Create user
    const { data: newUser, error } = await supabase
      .from("users")
      .insert([
        {
          email,
          password_hash: passwordHash,
          name,
          plan,
          department_id: departmentId,
        },
      ])
      .select()
      .single();

    if (error) throw error;

    return newUser;
  } catch (error) {
    console.error("Registration error:", error);
    throw error;
  }
}

export async function incrementWUSession(userId: string) {
  try {
    const { data: user } = await supabase
      .from("users")
      .select("wu_sessions_this_month, month_reset_date")
      .eq("id", userId)
      .single();

    if (!user) throw new Error("User not found");

    // Check if month has reset
    const lastReset = new Date(user.month_reset_date);
    const now = new Date();
    let sessions = user.wu_sessions_this_month;

    if (
      lastReset.getMonth() !== now.getMonth() ||
      lastReset.getFullYear() !== now.getFullYear()
    ) {
      sessions = 0;
      await supabase
        .from("users")
        .update({ month_reset_date: now.toISOString() })
        .eq("id", userId);
    }

    // Increment session count
    const { error } = await supabase
      .from("users")
      .update({ wu_sessions_this_month: sessions + 1 })
      .eq("id", userId);

    if (error) throw error;
  } catch (error) {
    console.error("WU session increment error:", error);
  }
}
