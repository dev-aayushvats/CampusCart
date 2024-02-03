package com.shadow.campuscarts

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.shadow.campuscarts.databinding.ActivityStartBinding

class StartActivity : AppCompatActivity() {
    private val binding: ActivityStartBinding by lazy {
        ActivityStartBinding.inflate(layoutInflater)
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        binding.nextButton.setOnClickListener {
            val intent = Intent(this, MainActivity::class.java)
            startActivity(intent)
        }
    }
}