package com.shadow.campuscarts

import android.os.Bundle
import android.os.Handler
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import kotlinx.coroutines.delay

@Suppress("DEPRECATION")
class SplashScreen : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash_screen)

        Handler().postDelayed({
            val intent = Intent(this, StartActivity::class.java)
            startActivity(intent)
            finish()
        }, 3000)
    }
}
