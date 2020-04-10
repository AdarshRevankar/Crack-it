
import java.util.*;

public class Main {
    public static HashMap<String, Integer> railCost = new HashMap<>();

    public static void main(String[] args) {

        // +-----------------------------------------------------+
        //                          INPUT
        // +-----------------------------------------------------+
        Scanner s = new Scanner(System.in);
        String[] locations = s.nextLine().split(" ");
        String source = locations[0];
        String destination = locations[1];
        String str = "";

        // To store the content
        TreeSet<String> vertices = new TreeSet<>();
        List<String> place_to_index = new ArrayList<>();

        // Store values in temporary list ( Hash-map )
        // Also make sure that all the nodes are present in the list
        vertices.add(source);
        vertices.add(destination);

        while (!(str = s.nextLine()).equals("")) {
            String[] inp = str.split(" ");

            // Check if input format is nor proper
            if (inp.length != 3)
                throw new InputMismatchException("Input Must contain : <Source destination Cost> format");

            // Extract key value pair
            String key = inp[0] + " " + inp[1];
            int value = Integer.parseInt(inp[2]);

            // Place to containers
            railCost.put(key, value);
            vertices.add(inp[0]);
            vertices.add(inp[1]);
        }

        // +-----------------------------------------------------+
        //                       PRE-PROCESS
        // +-----------------------------------------------------+
        // Assign a integer for each of the node
        for (String v: vertices){
            place_to_index.add(v);
        }
    }
}