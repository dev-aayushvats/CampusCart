package com.shadow.campuscarts.Fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import com.shadow.campuscarts.R
import com.shadow.campuscarts.adaptor.PopularAdapter
import com.shadow.campuscarts.databinding.FragmentHomeBinding  // Import the generated binding class

class HomeFragment : Fragment() {

    private lateinit var binding: FragmentHomeBinding  // Declare the binding variable

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment using the generated binding
        binding = FragmentHomeBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val foodName = listOf("Mango Lassi", "Sandwich", "Noodles", "Burger", "Manchurian")
        val price = listOf("$30","$25", "$45", "$60", "$60")
        val popularFoodImages =
            listOf(R.drawable.lassi, R.drawable.sandwich, R.drawable.noodle, R.drawable.burger, R.drawable.manchurian)
        val adapter = PopularAdapter(foodName, price, popularFoodImages)

        // Create an instance of LinearLayoutManager
        val linearLayoutManager = LinearLayoutManager(requireContext())

        // Set the layout manager for the RecyclerView
        binding.PopularRecyclerView.layoutManager = linearLayoutManager
        binding.PopularRecyclerView.adapter = adapter
    }

    companion object {
        // You can add companion object members here
    }
}
