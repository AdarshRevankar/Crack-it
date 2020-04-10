import java.util.*;

/**
 * Default Dictionary
 * Provides a Hash-Map
 * If there is not value for a certain key, it creates the value container from the previously specified type
 * This makes sure that the condition to check again if the value is present or not can be removed
 * @param <K>   Class type of the key to be stored
 * @param <V>   Class type of value to be stored
 */
class DefaultDict<K, V> extends HashMap<K, V> {

    Class<V> klass;

    public DefaultDict(Class klass) {
        this.klass = klass;
    }

    @Override
    public V get(Object key) {
        V returnValue = super.get(key);
        if (returnValue == null) {
            try {
                returnValue = klass.newInstance();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
            this.put((K) key, returnValue);
        }
        return returnValue;
    }
}

/**
 * Train - Class
 * Acts as a train which has certain cost for the path
 * Implements comparable object to sort the elements on the sorting criteria.
 * ie.
 *  1. Check the cost, low cost first
 *  2. if costs are same, then check the no. of stations it goes through, low first
 *  3. if cost & station counts are same, order them in alphabetical order
 */
class Train implements Comparable<Train> {
    private List<String> path;
    private int cost;

    Train(List<String> path, int cost) {
        this.path = path;
        this.cost = cost;
    }

    @Override
    public String toString() {
        // To print details in specified order
        // < station1 station2 ... cost >
        return String.join(" ", this.path) + " " + this.cost;
    }

    @Override
    public int compareTo(Train other) {
        if (this.cost < other.cost) {
            // First Condition
            return -1;
        } else if (this.cost == other.cost) {
            if (this.path.size() < other.path.size()) {
                // Second Condition
                return -1;
            } else if (this.path.size() == other.path.size()) {
                // Third condition
                return this.toString().compareTo(other.toString());
            }
        }
        return 1;
    }
}

/**
 * Graph - Computation
 * Selects the all possible route possible from {@link Graph} start to dest parametered integer
 * The Graph must contains the numbers as the inputs
 */
class Graph {
    private int vertices;
    private DefaultDict<Integer, List<Integer>> graph = null;
    List<Train> trains = new ArrayList<>();

    Graph(int vertices) {
        this.vertices = vertices;
        this.graph = new DefaultDict<>(ArrayList.class);
    }

    public void add_edge(int src, int dest) {
        // Adding a row to the source
        this.graph.get(src).add(dest);
    }

    private void get_path(int u, int d, boolean[] visited, List<Integer> path) {
        visited[u] = true;
        path.add(u);
        if (u == d) {
            // Convert from Integer list to String list
            List<String> p = new ArrayList<>(path.size());
            for (int i : path) {
                p.add(RailProblem.place_to_index.get(i));
            }

            // Add to the route list
            trains.add(new Train(p, RailProblem.get_cost(p)));
        } else {
            for (int i : this.graph.get(u)) {
                if (!visited[i]) {
                    // !!! Be very careful - to create a new instance of the path.
                    // Otherwise the same 'path' is modified by all the nodes which are visited which results in
                    // Wrong answer
                    this.get_path(i, d, visited, new ArrayList<>(path));
                }
            }
        }
        path.remove(0);
        visited[u] = false;
    }

    public void get_path_list(int start, int end){
        boolean[] visited = new boolean[this.vertices];
        List<Integer> path = new ArrayList<>();
        this.get_path(start, end, visited, path);
    }
}

public class RailProblem{
    public static HashMap<String, Integer> railCost = new HashMap<>();
    public static List<String> place_to_index = new ArrayList<>();

    public static int get_cost(List<String> path) {
        int cost = 0;
        for (int i = 0; i < path.size() - 1; i++) {
            String key = path.get(i) + " " + path.get(i + 1);
            cost += railCost.get(key);

        }
        return cost;
    }

    public static void main(String[] args) {

        // +-----------------------------------------------------+
        //                          INPUT
        // +-----------------------------------------------------+
        Scanner scan = new Scanner(System.in);
        String[] locations = scan.nextLine().split(" ");
        String source = locations[0];
        String destination = locations[1];
        String str = "";

        // To store the content
        TreeSet<String> vertices = new TreeSet<>();

        // Store values in temporary list ( Hash-map )
        // Also make sure that all the nodes are present in the list
        vertices.add(source);
        vertices.add(destination);

        while (!(str = scan.nextLine()).equals("")) {
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
        place_to_index.addAll(vertices);
        vertices.clear();

        // Create object of Graph
        Graph g = new Graph(place_to_index.size());

        for (String key : railCost.keySet()) {
            // Add edge from source
            String s = key.split(" ")[0];
            String d = key.split(" ")[1];
            g.add_edge(place_to_index.indexOf(s), place_to_index.indexOf(d));
        }

        // +-----------------------------------------------------+
        //                       CALCULATE
        // +-----------------------------------------------------+
        // Generate the list of Routes to the destination
        g.get_path_list(place_to_index.indexOf(source), place_to_index.indexOf(destination));

        // If there are no trains
        if(g.trains.size() == 0){
            System.out.println("No Trains");
        }
        else{
            // If there are trains
            // Sort the list according to the sorting criteria
            Collections.sort(g.trains);
            for (Train  t: g.trains) {
                // Print Trains details
                System.out.println(t);
            }
        }
    }
}
